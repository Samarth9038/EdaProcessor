# Streamlit Data Preprocessor & EDA Tool

An interactive **web-based data preprocessing and exploratory data analysis (EDA) tool** built using **Streamlit**. This application allows users to upload datasets and perform real-time data cleaning, transformation, and visualization — all without writing code.

---

## Features

### File Upload

* Upload CSV datasets directly through the UI
* Automatic session handling to preserve state across interactions

---

### Data Preprocessing

#### Numeric Features

* **Standardization** (StandardScaler)
* **Normalization / Scaling**
* Convert numeric columns to categorical

#### Categorical Features

* **Label Encoding**
* **One-Hot Encoding**

#### Missing Values Handling

* Fill missing values using:

  * Mean
  * Median
  * Mode
* Drop rows with missing values

#### Column Operations

* Drop unwanted columns instantly

---

### Exploratory Data Analysis (EDA)

* **Column-wise distribution visualization**

  * Histogram for numeric data
  * Bar charts for categorical data
* Quick preview of dataset (first 10 rows)
* Automatic detection of column data types

---

### Export

* Download the processed dataset as a CSV file

---

## Tech Stack

* **Frontend/UI:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Preprocessing:** Scikit-learn

---

## Installation

Install the required dependencies:

```bash
pip install streamlit pandas numpy scikit-learn
```

---

## ▶ Usage

1. **Run the app:**

   ```bash
   streamlit run app.py
   ```

2. **Upload your dataset**

   * Use the file uploader to select a CSV file

3. **Explore & preprocess**

   * View dataset preview
   * Apply transformations column-by-column
   * Handle missing values
   * Encode categorical variables
   * Scale numeric features

4. **Visualize data**

   * Click "Show Distribution" to view insights for each column

5. **Download processed data**

   * Export your cleaned dataset for further use

---

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── README.md          # Project documentation
```

---

## Key Highlights

* Interactive and beginner-friendly UI
* No coding required for preprocessing
* Real-time updates using Streamlit session state
* Modular and extendable design

---

## Future Improvements

* Correlation heatmap and advanced visualizations
* Undo/redo preprocessing steps
* ML model training integration
* Smart preprocessing suggestions
* Feature importance insights

---

## 📜 License

This project is open-source and available under the MIT License.
