import streamlit as st
from typing import List, Dict, Tuple
import time
from sympy import symbols, And, Or
from sympy.logic import satisfiable
from sympy.logic.boolalg import to_cnf
from itertools import combinations

# Page configuration
st.set_page_config(
    page_title="🏥 FOL Diagnostic Chatbot",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Model ---

# Initialize session state
if 'knowledge_base' not in st.session_state:
    st.session_state.knowledge_base = {}
if 'custom_rules' not in st.session_state:
    st.session_state.custom_rules = []

# Define symptom symbols for FOL
DIAGNOSTIC_QUESTIONS = [
    {"key": "fever", "text": "Do you have a fever (body temperature above 98.6°F)?"},
    {"key": "cough", "text": "Do you have a cough?"},
    {"key": "sore_throat", "text": "Do you have a sore throat?"},
    {"key": "runny_nose", "text": "Do you have a runny or stuffy nose?"},
    {"key": "body_aches", "text": "Do you experience body aches or muscle pain?"},
    {"key": "fatigue", "text": "Do you feel unusually tired or fatigued?"},
    {"key": "headache", "text": "Do you have a headache?"},
    {"key": "sneezing", "text": "Do you have frequent sneezing?"},
    {"key": "itchy_eyes", "text": "Do you have itchy or watery eyes?"},
    {"key": "sensitivity_to_light", "text": "Are you sensitive to light?"},
    {"key": "nausea", "text": "Do you feel nauseous or have an upset stomach?"},
    {"key": "persistent_cough", "text": "Do you have a persistent cough (lasting more than a week)?"},
    {"key": "chest_discomfort", "text": "Do you feel chest discomfort or chest pain?"},
    {"key": "swollen_tonsils", "text": "Do you have swollen tonsils?"}
]

SYMPTOM_SYMBOLS = {q["key"]: symbols(q["key"]) for q in DIAGNOSTIC_QUESTIONS}

# Symptom name mapping
SYMPTOM_NAMES = {q["key"]: q["text"].split("?")[0] for q in DIAGNOSTIC_QUESTIONS}

# Built-in diagnostic rules using FOL
BUILT_IN_RULES = [
    {
        "name": "Common Cold",
        "conditions": ["sore_throat", "runny_nose", "cough"],
        "min_conditions": 2,
        "confidence": 0.7,
    },
    {
        "name": "Flu",
        "conditions": ["fever", "body_aches", "cough", "fatigue"],
        "min_conditions": 3,
        "confidence": 0.8,
    },
    {
        "name": "Allergies",
        "conditions": ["runny_nose", "sneezing", "itchy_eyes"],
        "min_conditions": 2,
        "confidence": 0.75,
    },
    {
        "name": "Migraine",
        "conditions": ["headache", "sensitivity_to_light", "nausea"],
        "min_conditions": 2,
        "confidence": 0.8,
    },
    {
        "name": "Bronchitis",
        "conditions": ["persistent_cough", "chest_discomfort", "fatigue"],
        "min_conditions": 2,
        "confidence": 0.75,
    },
    {
        "name": "Strep Throat",
        "conditions": ["sore_throat", "fever", "swollen_tonsils"],
        "min_conditions": 2,
        "confidence": 0.85,
    }
]

def build_fol_expression(rule: Dict) -> Tuple:
    """Build a First Order Logic expression for a diagnostic rule."""
    symptoms = [SYMPTOM_SYMBOLS[cond] for cond in rule["conditions"]]
    min_conditions = rule["min_conditions"]
    
    if len(symptoms) < min_conditions:
        return None, "Invalid rule"

    # Create expression for "at least min_conditions are true"
    combos = list(combinations(symptoms, min_conditions))
    expr = Or(*[And(*combo) for combo in combos])
    
    # Create a human-readable version
    condition_names = [SYMPTOM_NAMES.get(c.name, c.name) for c in symptoms]
    readable_combos = list(combinations(condition_names, min_conditions))
    combo_strs = ["(" + " ∧ ".join(combo) + ")" for combo in readable_combos]
    readable = " ∨ ".join(combo_strs)
    
    return expr, readable

def evaluate_fol_rule(rule: Dict, kb: Dict[str, bool]) -> Tuple[bool, float, List[str]]:
    """Evaluate a rule using FOL, returning satisfaction, confidence, and matched symptoms."""
    expr, _ = build_fol_expression(rule)
    if expr is None:
        return False, 0.0, []

    # Substitute known facts into the expression
    subs_dict = {SYMPTOM_SYMBOLS[s]: v for s, v in kb.items() if s in rule["conditions"]}
    
    if expr.subs(subs_dict) == True:
        matched_symptoms = [s for s, v in kb.items() if v and s in rule["conditions"]]
        confidence = rule["confidence"] * (len(matched_symptoms) / len(rule["conditions"]))
        return True, confidence, matched_symptoms
    
    return False, 0.0, []

def forward_chaining_fol(kb: Dict[str, bool], rules: List[Dict]) -> List[Tuple]:
    """Apply forward chaining using FOL to generate diagnoses."""
    diagnoses = []
    for rule in rules:
        is_satisfied, confidence, matched_symptoms = evaluate_fol_rule(rule, kb)
        if is_satisfied:
            _, readable_expr = build_fol_expression(rule)
            diagnoses.append((
                rule["name"],
                confidence,
                len(matched_symptoms),
                len(rule["conditions"]),
                matched_symptoms,
                readable_expr
            ))
    diagnoses.sort(key=lambda x: x[1], reverse=True)
    return diagnoses

def check_logical_consistency(kb: Dict[str, bool]) -> Tuple[bool, str]:
    """Check if the knowledge base is logically consistent."""
    if not kb:
        return True, "Knowledge base is empty."
    
    facts = [SYMPTOM_SYMBOLS[s] if v else ~SYMPTOM_SYMBOLS[s] for s, v in kb.items()]
    if not satisfiable(And(*facts)):
        return False, "Knowledge base contains contradictions!"
    return True, "Knowledge base is logically consistent."

# --- View ---

st.title("🏥 Diagnostic Chatbot with First Order Logic")
st.markdown("An interactive medical assistant using `sympy` for formal logic.")
st.markdown("---")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["🏠 Home", "💬 Diagnostic Interview", "📋 Knowledge Base", 
     "🔍 Diagnosis", "🧮 FOL Expressions", "➕ Add Custom Rule", "🔄 Reset"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Session Stats")
positive_symptoms = sum(1 for v in st.session_state.knowledge_base.values() if v)
st.sidebar.metric("Symptoms Collected", positive_symptoms)
st.sidebar.metric("Diagnoses Available", len(BUILT_IN_RULES) + len(st.session_state.custom_rules))
st.sidebar.metric("Custom Rules", len(st.session_state.custom_rules))

is_consistent, consistency_msg = check_logical_consistency(st.session_state.knowledge_base)
st.sidebar.markdown(f"**KB Status:** {'✅ Consistent' if is_consistent else '❌ Inconsistent'}")

# Page routing
if page == "🏠 Home":
    st.header("Welcome to the FOL-Powered Diagnostic Chatbot! 👋")
    st.markdown("""
    This application demonstrates how **First Order Logic (FOL)** can be used to build a simple diagnostic system. 
    It uses the `sympy` library to perform logical inference.
    
    **How it works:**
    1.  You answer questions about your symptoms.
    2.  Each answer becomes a logical fact in a **Knowledge Base** (e.g., `fever = True`).
    3.  Diagnostic rules, written as **FOL expressions**, are evaluated against the knowledge base.
    4.  If a rule's conditions are met, a potential diagnosis is suggested.
    
    Go to the **Diagnostic Interview** to get started!
    """)
    st.warning("This tool is for educational purposes only and is not a substitute for professional medical advice.")

elif page == "💬 Diagnostic Interview":
    st.header("💬 Diagnostic Interview")
    st.markdown("Please answer the following questions. Your answers will build the logical knowledge base.")
    
    for i, question in enumerate(DIAGNOSTIC_QUESTIONS):
        st.markdown(f"**Question {i+1}:** {question['text']}")
        
        answer = st.radio(
            "Your answer:", ["Select", "Yes", "No"],
            key=f"q_{question['key']}",
            index=["Select", "Yes", "No"].index(
                "Yes" if st.session_state.knowledge_base.get(question["key"]) is True else
                "No" if st.session_state.knowledge_base.get(question["key"]) is False else
                "Select"
            ),
            horizontal=True
        )
        
        if answer == "Yes":
            st.session_state.knowledge_base[question["key"]] = True
        elif answer == "No":
            st.session_state.knowledge_base[question["key"]] = False

elif page == "📋 Knowledge Base":
    st.header("📋 Knowledge Base")
    st.markdown("These are the logical facts collected from your answers.")
    
    is_consistent, msg = check_logical_consistency(st.session_state.knowledge_base)
    st.info(f"**Consistency Check:** {msg}")

    if not st.session_state.knowledge_base:
        st.info("No facts collected yet. Please complete the interview.")
    else:
        st.subheader("Facts:")
        for symptom, value in st.session_state.knowledge_base.items():
            st.code(f"{symptom} = {value}", language="python")

elif page == "🔍 Diagnosis":
    st.header("🔍 Diagnosis Results")
    st.markdown("Diagnoses are inferred by applying FOL rules to the knowledge base.")
    
    if not st.session_state.knowledge_base:
        st.warning("Please complete the interview to get a diagnosis.")
    else:
        all_rules = BUILT_IN_RULES + st.session_state.custom_rules
        diagnoses = forward_chaining_fol(st.session_state.knowledge_base, all_rules)
        
        if not diagnoses:
            st.info("No diagnosis could be inferred from the current symptoms.")
        else:
            for name, confidence, matched, total, matched_symptoms, fol_expr in diagnoses:
                with st.expander(f"**{name}** - {confidence*100:.1f}% confidence", expanded=True):
                    st.progress(confidence)
                    st.markdown(f"**Matched Symptoms:** {matched}/{total}")
                    st.markdown(f"**FOL Rule:** `{fol_expr}`")
                    st.markdown("**Satisfied by:**")
                    for symptom in matched_symptoms:
                        st.markdown(f"- `{symptom} = True`")

elif page == "🧮 FOL Expressions":
    st.header("🧮 First Order Logic Expressions")
    st.markdown("These are the formal logic rules used for diagnosis.")
    
    all_rules = BUILT_IN_RULES + st.session_state.custom_rules
    for rule in all_rules:
        st.subheader(rule["name"])
        expr, readable = build_fol_expression(rule)
        st.markdown(f"**Requires at least {rule['min_conditions']} of {len(rule['conditions'])} symptoms.**")
        st.markdown("**SymPy Expression (CNF):**")
        st.code(str(to_cnf(expr)), language="python")
        st.markdown("**Human-Readable:**")
        st.code(readable, language="text")

elif page == "➕ Add Custom Rule":
    st.header("➕ Add Custom Diagnostic Rule")
    with st.form("custom_rule_form"):
        rule_name = st.text_input("Rule Name *")
        
        selected_symptoms = st.multiselect(
            "Select Symptoms *",
            options=list(SYMPTOM_NAMES.keys()),
            format_func=lambda x: SYMPTOM_NAMES[x]
        )
        
        min_conditions = st.number_input(
            "Minimum Required Symptoms *",
            min_value=1,
            max_value=len(selected_symptoms) if selected_symptoms else 1,
            value=1
        )
        
        confidence = st.slider("Base Confidence *", 0.0, 1.0, 0.75)
        
        if st.form_submit_button("Add Rule"):
            if rule_name and selected_symptoms and min_conditions:
                new_rule = {
                    "name": rule_name,
                    "conditions": selected_symptoms,
                    "min_conditions": min_conditions,
                    "confidence": confidence
                }
                st.session_state.custom_rules.append(new_rule)
                st.success(f"Rule '{rule_name}' added!")
            else:
                st.error("Please fill all required fields.")

elif page == "🔄 Reset":
    st.header("🔄 Reset Session")
    st.warning("This will clear the knowledge base and reset the interview.")
    if st.button("Confirm Reset", type="primary"):
        st.session_state.knowledge_base = {}
        st.success("Session has been reset.")
        time.sleep(1)
        st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #626C71; font-size: 12px;'>"
    "FOL Diagnostic Chatbot v2.0 | Educational Demo"
    "</div>",
    unsafe_allow_html=True
)