# 🌙 Airbnb Dynamic Pricing Optimizer
### A Prescriptive Analytics App for Revenue-Maximizing Nightly Pricing

This project applies **prescriptive analytics, optimization modeling, and interactive visualization** to determine the **optimal nightly price** for Airbnb listings in Boston neighborhoods.  
The result is a fully deployed **Streamlit web application**, backed by a custom optimization engine using demand elasticity parameters.

---

## 📌 1. Project Overview
Pricing short-term rentals is difficult — set the price too high and demand drops; too low and revenue is lost.  
This app helps hosts choose the **revenue-maximizing nightly price** based on:

- Neighborhood-specific demand parameters  
- Price elasticity  
- Historical occupancy patterns  
- Valid price bounds  

The model feeds an optimization function that minimizes the negative revenue (i.e., maximizes revenue).

---

## 🧩 2. Business Problem
Airbnb hosts often price listings based on intuition or simple heuristics. This leads to:

- Underpricing during high demand  
- Overpricing during slower periods  
- Missed revenue opportunities  

**Goal:**  
Use prescriptive analytics to compute the **optimal nightly rate** that maximizes expected monthly revenue.

**Why it matters:**  
Small price adjustments (even $5–$15) can significantly impact monthly revenue due to compounding effects across bookings.

---

## 📊 3. Methodology
We assume a linear demand model:

### **Demand Function**
\[
\text{occupancy}(p) = a - b \cdot p
\]

Where:  
- **a** = demand intercept  
- **b** = price sensitivity  
- **p** = price  

### **Revenue Function**
\[
\text{revenue}(p) = p \times \text{occupancy}(p) \times 30
\]

### **Optimization Objective**
\[
\max_p \; p(a - bp) \times 30
\]

### **Constraints**
\[
p_{\min} \le p \le p_{\max}
\]

### Solver
Streamlit Cloud does not support Gurobi, so the model uses:

- **SciPy L-BFGS-B optimizer**  
- Objective expressed as a minimization of negative revenue  

---

## 🖥 4. Streamlit Application Features
The deployed app allows users to:

### ✔️ Select Airbnb Neighborhood
Dropdown generated from `demand_params.csv`.

### ✔️ Adjust Demand Model Inputs
Tune **a** and **b** parameters interactively.

### ✔️ Set Price Bounds
Minimum and maximum acceptable nightly rate.

### ✔️ Run Optimization
Returns:
- Optimal price  
- Expected occupancy  
- Monthly revenue  

### ✔️ Interactive Visualizations
- Revenue curve (price vs. revenue)  
- Demand curve (price vs. occupancy)  
- Optimal point highlighted  

---

## 📂 5. Repository Structure

```
airbnb_pricing_optimizer/
│ app.py
│ optimizer.py
│ requirements.txt
│ demand_params.csv
│ listings.csv
│ README.md
```

---

## 🌐 6. Deployed Application
The live application is hosted on Streamlit Cloud:

👉 **https://airbnbpricingoptimizer-7npyw9z94mecmhwf97bprr.streamlit.app/**


To demonstrate the functionality of the app:

1. Open the deployed app.  
2. Select a neighborhood from the dropdown.  
3. Adjust the price range or keep defaults.  
4. Click **Optimize Price**.  
5. The app will display:
   - Optimal price
   - Expected occupancy
   - Monthly revenue
6. Scroll down to view:
   - Revenue vs Price curve
   - Demand vs Price curve

   image.png


7 Run Locally
To run the app locally:

### **Clone the repository**
```bash
git clone https://github.com/Abdelmou1987/airbnb_pricing_optimizer.git
cd airbnb_pricing_optimizer
```

### **Install dependencies**
```bash
pip install -r requirements.txt
```

### **Launch Streamlit**
```bash
streamlit run app.py
```

---

## 💡 8. Managerial Insights
From the optimizer’s outputs:

- Hosts can set prices that **maximize monthly revenue**, not occupancy alone.  
- Higher sensitivity neighborhoods (larger **b**) require more conservative pricing.  
- Lower sensitivity neighborhoods (small **b**) allow premium pricing.  
- Demand-based pricing prevents leaving money on the table during high occupancy seasons.

### **When to adjust pricing:**
- Event weeks (Marathon, holidays)  
- Off-peak seasons  
- Long-term stay discounts  
- Improving listing ratings → higher price tolerance  

---

## 🚀 9. Limitations & Future Enhancements
Planned improvements:

- Use real Airbnb API for dynamic data  
- Seasonal demand modeling  
- Multi-objective optimization (rating + revenue)  
- Price clustering by property type  
- Better nonlinear demand functions  

---

## 🏁 Conclusion
This project demonstrates the application of **prescriptive analytics** to solve real-world pricing problems, combining data, optimization, and an interactive web tool into one professional-grade solution.
