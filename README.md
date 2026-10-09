# 🌦️ AtmoSync — Micro-Climate Arbitrage Analytics

**An end-to-end Data Analytics project exploring the relationship between micro-climate conditions, air quality, energy demand, energy prices, and climate-driven business opportunities.**

![Python](https://img.shields.io/badge/Python-Analysis-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Data%20Analysis-blue?logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi&logoColor=black)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-Streaming-black?logo=apachekafka&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-Cloud%20Data%20Platform-29B5E8?logo=snowflake&logoColor=white)

## 📌 Project Overview

AtmoSync is a data analytics project designed to investigate how changing micro-climate conditions influence environmental indicators and energy-related metrics across cities.

The project uses a structured climate dataset containing approximately **12,000 records and 27 columns** to explore temperature, humidity, Air Quality Index (AQI), energy demand, energy prices, and climate opportunity scores.

The objective is to transform raw climate and energy data into meaningful insights through data cleaning, exploratory data analysis (EDA), statistical analysis, SQL-based data transformations, and interactive Power BI visualizations.

The project is being developed toward an end-to-end analytics workflow incorporating data streaming and cloud data warehousing.

## 🎯 Project Objectives

- Analyze climate conditions and environmental indicators across cities.
- Identify patterns in temperature, humidity, and air pollution.
- Explore relationships between climate variables and energy demand.
- Examine energy price variations and potential climate-related opportunities.
- Apply data cleaning, exploratory analysis, and statistical techniques.
- Develop a Power BI dashboard to communicate key findings.
- Build practical experience with Kafka-based streaming and Snowflake data warehousing.

## 📊 Dataset Description

**Dataset:** `AtmoSync_Micro_Climate_Analytics_12000.csv`

| Attribute | Description |
|---|---|
| Record_ID | Unique identifier for each record |
| Date / Time | Date and time associated with an observation |
| City | City associated with the observation |
| Temperature_C | Temperature in degrees Celsius |
| Humidity_Percent | Relative humidity percentage |
| AQI | Air Quality Index |
| Energy_Demand_MW | Energy demand in megawatts |
| Energy_Price_INR_kWh | Energy price in INR per kWh |
| Pollution_Level | Categorized pollution indicator |
| Climate_Opportunity_Score | Score representing a potential climate-related opportunity |

*Note: This table lists representative fields. Refer to `docs/data_dictionary.md` for the complete schema and verified column definitions.*

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Jupyter Notebook | Exploratory analysis and documentation |
| SQL | Data querying, aggregation, and transformations |
| Apache Kafka | Planned or implemented event-stream processing |
| Snowflake | Planned or implemented cloud data warehousing |
| Power BI | Interactive dashboard and KPI reporting |
| Git & GitHub | Version control and project documentation |
| VS Code | Development environment |

## 🔍 Analytical Workflow

### 1. Data Loading and Understanding
- Load the CSV dataset using Pandas.
- Inspect the dataset dimensions, columns, data types, and sample records.
- Review missing values, duplicate records, and data quality issues.

### 2. Data Cleaning and Preparation
- Check and handle missing or invalid values where appropriate.
- Identify duplicate records and inconsistent data types.
- Validate date, time, and numerical columns.
- Prepare the dataset for exploratory analysis and visualization.

### 3. Exploratory Data Analysis (EDA)
The analysis focuses on:

- **City Analysis:** Compare climate and energy indicators across cities.
- **Temperature Analysis:** Examine temperature distributions and variations.
- **Humidity Analysis:** Investigate humidity patterns and their relationship with other variables.
- **Air Quality Analysis:** Compare AQI levels and pollution indicators.
- **Energy Demand Analysis:** Explore energy consumption patterns across observations.
- **Energy Price Analysis:** Examine variations in energy prices.
- **Opportunity Score Analysis:** Investigate how the climate opportunity score varies across cities and conditions.

### 4. SQL Analysis
SQL is used in the planned analytics workflow to support structured querying, aggregations, and data transformations. The completed SQL analysis will be documented here as the relevant queries and outputs are validated.

### 5. Streaming and Cloud Data Pipeline
The intended architecture incorporates:

- **Apache Kafka:** Stream climate records through a producer-consumer workflow.
- **Snowflake:** Store incoming records in a RAW layer and organize processed data into staging and analytics layers.
- **Data Validation:** Verify record counts, schema consistency, and transformations between pipeline stages.

The pipeline components and their integration status will be documented as implementation and testing progress.

### 6. Power BI Dashboard
An interactive Power BI dashboard has been created to present key climate and energy indicators.

The dashboard is intended to help users explore:

- Key performance indicators (KPIs).
- Climate variations across cities.
- Temperature, humidity, and AQI patterns.
- Energy demand and energy price trends.
- Climate opportunity scores.

Dashboard metrics and conclusions should be interpreted using the definitions and filters provided in the report.

## 📈 Dashboard Preview

The Power BI dashboard provides a visual overview of the project's climate and energy metrics.

**Dashboard screenshot:**

![(https://github.com/PournamiManthodi/AtmoSync/blob/main/AtmoSync_Dashboard.pbix)](https://github.com/PournamiManthodi/AtmoSync/blob/main/AtmoSync_Dashboard.pbix)

**Power BI report file:** `dashboard/AtmoSync_Dashboard.pbix`

Open the `.pbix` file using Microsoft Power BI Desktop to explore the report.

*Ensure both dashboard files exist at these paths in your repository. Replace the screenshot reference if your image has a different filename.*

## 🏗️ Project Architecture

The intended end-to-end workflow is:

```text
Climate & Energy Dataset (CSV)
              |
              v
     Python Data Processing
              |
              v
    Exploratory Data Analysis
              |
              v
     Kafka Producer / Stream
              |
              v
       Kafka Consumer
              |
              v
     Snowflake RAW Layer
              |
              v
   STAGING & ANALYTICS Layers
              |
              v
       Power BI Dashboard
              |
              v
       Business Insights
```

**Architecture note:** This diagram represents the target workflow. It should not be interpreted as proof that every component is fully integrated. Update the diagram to reflect the actual working connections as the pipeline is completed.

## 📁 Repository Structure

```text
AtmoSync/
│
├── data/
│   └── AtmoSync_Micro_Climate_Analytics_12000.csv
│
├── analysis/
│   └── exploratory_analysis.ipynb
│
├── simulator/
│   └── csv_stream_simulator.py
│
├── dashboard/
│   ├── AtmoSync_Dashboard.pbix
│   └── AtmoSync_Dashboard.png
│
├── docs/
│   └── data_dictionary.md
│
├── requirements.txt
└── README.md
```

This structure reflects the intended organization of the project. Keep only files that exist in your repository, and add SQL scripts or pipeline configuration files as they are implemented.

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or a compatible version for the project's dependencies.
- Git.
- Visual Studio Code or another Python editor.
- Jupyter Notebook.
- Microsoft Power BI Desktop to open the dashboard.
- Kafka and Snowflake access if running the streaming and cloud pipeline components.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AtmoSync
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Ensure `requirements.txt` contains the Python packages required by the code in your repository.

### 4. Run the Exploratory Analysis

Open the notebook:

```text
analysis/exploratory_analysis.ipynb
```

Run the cells sequentially to reproduce the data inspection and analysis. Confirm that the dataset path in the notebook matches the repository structure.

### 5. Run the CSV Stream Simulator

If the simulator and its dependencies are configured, open a terminal in the `simulator` directory and run:

```bash
python csv_stream_simulator.py
```

If Kafka integration is enabled, ensure the Kafka broker is running and the producer configuration matches your environment.

### 6. Open the Dashboard

Open `dashboard/AtmoSync_Dashboard.pbix` in Power BI Desktop.

If the report uses local file paths, update the data source settings to point to the appropriate dataset on your computer.

*Snowflake credentials, Kafka connection details, and other secrets must be configured locally or through secure environment variables. Never commit credentials to GitHub.*

## 📌 Key Deliverables

- Structured climate and energy dataset.
- Python-based data exploration and cleaning.
- Exploratory data analysis and visualizations.
- SQL analytics and transformation workflow.
- Kafka streaming component.
- Snowflake data warehouse design and integration.
- Power BI dashboard for climate and energy indicators.
- Documentation of the dataset, workflow, and analytical findings.

Deliverables that are still being developed should remain marked as planned or in progress.

## 💡 Expected Business Value

AtmoSync explores how environmental and energy indicators can be analyzed together to support data-informed decisions.

Potential applications include:

- Comparing climate conditions across cities.
- Monitoring environmental indicators.
- Understanding patterns in energy demand and prices.
- Identifying observations with higher climate opportunity scores.
- Communicating findings through interactive dashboards.

These are analytical objectives, not claims of proven financial returns or validated arbitrage opportunities. Any such conclusion would require additional evidence and validation.

## 🚧 Current Project Status

**Status: In Progress**

| Component | Status |
|---|---|
| Dataset preparation | Developed; continue validating data quality |
| Python EDA | Developed; verify notebook reproducibility |
| CSV stream simulator | Implemented as a development component; verify Kafka integration |
| Kafka pipeline | Verify producer-consumer integration |
| Snowflake warehouse | Verify table creation, ingestion, and transformations |
| Power BI dashboard | Created |
| End-to-end testing | Pending validation |
| Final documentation | In progress |

Update the status table to reflect the actual working state of each component.

## 🔮 Future Improvements

- Complete and test the end-to-end Kafka-to-Snowflake integration.
- Automate data validation and ingestion monitoring.
- Expand SQL transformations and analytical views.
- Improve dashboard interactivity and drill-down analysis.
- Add reproducible data quality checks.
- Document validated findings and recommendations.
- Explore predictive analytics for energy demand and climate indicators.

## 👩‍💻 Author

**Pournami Manthodi**

Aspiring Data Analyst | Data Analytics & Data Science

- **GitHub:** [PournamiManthodi](https://github.com/PournamiManthodi)
- **LinkedIn:** [Connect with me](https://www.linkedin.com/in/pournamimanthodi/)

## ⭐ Acknowledgements

This project is developed as a hands-on learning initiative to strengthen practical skills in data analytics, data engineering concepts, data visualization, and business-oriented problem solving.

If you find this project useful, feel free to explore the repository and share feedback.
