# 🌙 Airbnb Dynamic Pricing Optimizer  
### ISOM-839 — Prescriptive Analytics  
### By: Mutaz Abdel Dayem

---

## 📌 1. Project Overview
This project builds a prescriptive analytics product that helps Airbnb hosts choose the optimal nightly price to maximize revenue. 

The tool uses:
- a demand elasticity model  
- a concave revenue function  
- nonlinear optimization (Gurobi or SciPy)  
- an interactive Streamlit web application  

---

## 📊 2. Business Problem
Setting prices manually often leads to:
- High vacancy when priced too high
- Lost revenue when priced too low

This optimizer recommends the *price that maximizes expected monthly revenue* for each neighborhood.

---

## 🧠 3. Methodology

### Demand Model:
\[
D(p) = a - bp
\]

### Revenue Model:
\[
R(p) = p(a - bp)
\]

### Optimization:
\[
\max_p \; ap - bp^2
\]

Subject to:
\[
p_{\min} \le p \le p_{\max}
\]

---

## 🖥 4. Streamlit App Features
- Neighborhood selector  
- User-selected pricing bounds  
- Auto-loaded demand parameters  
- Price optimization  
- Revenue curve with optimal point  
- Demand curve visualization  
- Business recommendations  

---

## 📂 5. Repository Structure

