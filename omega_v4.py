# OMEGA v4.0 - HYBRID AUTONOMOUS INTELLIGENCE
# Architect: Owoicho Emmanuel | License: MIT

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

class PHOENIX:
    @staticmethod
    def run(data):
        print("\n[PHOENIX] AUTO-CLEAN")
        cleaned = data.copy().drop_duplicates()
        for col in cleaned.select_dtypes(include=np.number).columns:
            cleaned[col] = cleaned[col].fillna(cleaned[col].median())
            q1, q3 = cleaned[col].quantile(0.01), cleaned[col].quantile(0.99)
            cleaned[col] = cleaned[col].clip(q1, q3)
        print(f"Cleaned: {data.shape} -> {cleaned.shape}")
        return cleaned

class SENTINEL:
    @staticmethod
    def run(data):
        print("\n[SENTINEL] VALIDATION")
        checks = {"empty": bool(data.empty), "duplicates": int(data.duplicated().sum()), "missing": int(data.isna().sum().sum())}
        print(checks); return checks

class MATRIX:
    @staticmethod
    def run(data):
        print("\n[MATRIX] STATISTICAL ANALYSIS")
        print("Means:\n", data.mean(numeric_only=True).round(2))
        print("Correlation:\n", data.corr(numeric_only=True).round(3))
        return {"mean": data.mean(numeric_only=True), "corr": data.corr(numeric_only=True)}

class TITAN:
    @staticmethod
    def run(data, target):
        print("\n[TITAN] AUTO-MODEL SELECTION")
        X = data.drop(columns=[target]); y = data[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        lin = LinearRegression(); lin.fit(X_train, y_train)
        r2_lin = r2_score(y_test, lin.predict(X_test))
        rf = RandomForestRegressor(n_estimators=150, random_state=42, n_jobs=-1)
        rf.fit(X_train, y_train)
        pred_rf = rf.predict(X_test); r2_rf = r2_score(y_test, pred_rf)
        print(f"Linear R2={r2_lin:.4f} | RF R2={r2_rf:.4f}")
        if r2_lin >= r2_rf:
            winner, pred, name, r2 = lin, lin.predict(X_test), "LinearRegression", r2_lin
        else:
            winner, pred, name, r2 = rf, pred_rf, "RandomForestRegressor", r2_rf
        metrics = {"Best_Model": name, "R2": float(r2), "RMSE": float(np.sqrt(mean_squared_error(y_test, pred))), "MAE": float(mean_absolute_error(y_test, pred))}
        print(f"WINNER: {name} -> {metrics}")
        return winner, metrics

class NEXUS:
    @staticmethod
    def run(metrics):
        r2 = metrics["R2"]
        assessment = "Strong predictive fit" if r2 >= 0.8 else "Moderate predictive fit" if r2 >= 0.5 else "Weak predictive fit"
        print("\n[NEXUS] Decision:", assessment); return assessment

class SYNAPSE:
    @staticmethod
    def run(stats, metrics, assessment):
        return {"stats": str(stats), "metrics": metrics, "decision": assessment}

class ORACLE:
    @staticmethod
    def run(report):
        print("\n[ORACLE] INTELLIGENCE REPORT")
        print("Decision:", report["decision"]); print("Performance:", report["metrics"])
        pd.DataFrame([report["metrics"]]).to_csv("omega_report.csv", index=False)
        with open("omega_report.txt", "w") as f:
            f.write(f"OMEGA v4.0 REPORT\nDecision: {report['decision']}\nMetrics: {report['metrics']}\n")
        print("Saved: omega_report.csv + omega_report.txt")

class OMEGA:
    @staticmethod
    def run():
        print("="*60); print("OMEGA v4.0"); print("HYBRID AUTONOMOUS INTELLIGENCE"); print("ARCHITECT: OWOICHO EMMANUEL"); print("="*60)
        for i, name in enumerate(["MATRIX","PHOENIX","TITAN","NEXUS","SYNAPSE","SENTINEL","ORACLE"], 1):
            print(f"[{i:02d}] {name:<10} — INITIALIZING")
        try:
            data = pd.read_csv("data.csv"); print(f"\n[AUTO-CSV] Loaded data.csv: {data.shape}")
        except FileNotFoundError:
            np.random.seed(42)
            data = pd.DataFrame({"size": np.random.randint(500, 4000, 300), "bedrooms": np.random.randint(1, 6, 300), "age": np.random.randint(1, 30, 300)})
            data["price"] = 150*data["size"] + 20000*data["bedrooms"] - 900*data["age"] + np.random.normal(0, 12000, 300)
            print("\n[AUTO-CSV] No data.csv -> Demo data loaded")
        cleaned = PHOENIX.run(data); SENTINEL.run(cleaned); statistics = MATRIX.run(cleaned)
        model, metrics = TITAN.run(cleaned, "price"); assessment = NEXUS.run(metrics)
        report = SYNAPSE.run(statistics, metrics, assessment); ORACLE.run(report)
        print("\n"+"="*60); print("OMEGA v4.0 EXECUTION FINISHED"); print("="*60); return report

if __name__ == "__main__":
    OMEGA.run()
