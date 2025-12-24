import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

import streamlit as st
from src.preprocess import normalize
from src.matchers import tfidf_match_score, sim_to_score
from src.skills import missing_skills

st.title("AI Resume Matcher")

resume = st.text_area("Paste Resume Text", height=200)
job = st.text_area("Paste Job Description", height=200)

if st.button("Compute Match") and resume and job:
    r = normalize(resume)
    j = normalize(job)

    sim = tfidf_match_score(r, j)
    score = sim_to_score(sim)
    miss, matched = missing_skills(r, j)

    st.metric("Match score", f"{score}/100")
    st.write("Matched skills:", matched)
    st.write("Missing skills:",miss)