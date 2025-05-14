# Customer Segmentation for E-Commerce

## Description
This project analyzes transactional data from a UK-based online retailer to segment customers using clustering algorithms. The primary goal is to enhance marketing effectiveness and increase sales by identifying distinct customer profiles based on their purchasing behavior.

## Dataset
The dataset is sourced from the **UCI Machine Learning Repository** and contains transactions from 2010 to 2011. It includes the following columns:

- **Invoice**: Unique identifier for each transaction. If it starts with 'C', it indicates a cancellation.
- **StockCode**: Unique code assigned to each product.
- **Description**: Product description.
- **Quantity**: Number of units purchased in the transaction.
- **InvoiceDate**: Date and time of the transaction.
- **UnitPrice**: Unit price of the product in pounds sterling.
- **Customer ID**: Unique customer identifier.
- **Country**: Customer's country.

Link to the dataset: [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)

The file used in this project is `online_retail_II.xlsx`, specifically the sheet `Year 2010-2011`.

## Methodology
The analysis was conducted in the following stages:

1. **Data Cleaning**:
   - Removed null values (24.93% in `Customer ID` and 0.27% in `Description`).
   - Removed duplicates (5,225 duplicate rows identified).
   - Handled canceled transactions (2.21% of the total).
   - Cleaned the `Description` column by removing rows containing service descriptions to focus solely on product transactions.
   - Corrected inconsistencies where multiple `StockCode` were associated with a single description and vice versa.
   - Treated zero unit prices by removing or correcting entries to avoid distortions in the analysis.

2. **Feature Engineering**:
   - Created customer-centric features, including:
     - **Recency**: Days since the last purchase.
     - **Total_Transactions**: Total number of transactions per customer.
     - **Total_Products_Purchased**: Total products purchased.
     - **Total_Spend**: Total expenditure per customer.
     - **Average_Transaction_Value**: Average value per transaction.
     - **Unique_Products_Purchased**: Number of unique products purchased.
     - **Cancellation_Frequency**: Total number of canceled transactions.
     - **Cancellation_Rate**: Proportion of canceled transactions.
     - **Monthly_Spending_Mean**: Average monthly spending.
     - **Monthly_Spending_Std**: Standard deviation of monthly spending.

3. **Clustering**:
   - Applied the K-means algorithm to segment customers based on the generated features.

## Results
[To be updated with specific results from the clustering analysis.]

## Visualizations
Visualizations generated during the analysis include:
- Scatter plots to explore relationships between features such as `Recency`, `Total_Spend`, and `Total_Transactions`.
- Representations of the resulting clusters (screenshots or links to graphs in the notebook are recommended).

These visualizations are available in the notebook `e-commerce_RFM_Segmentation.ipynb`.

## Requirements
To run this project, ensure you have the following dependencies installed:
- Python 3.12+
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- scikit-learn (for K-means)
- openpyxl (to read `.xlsx` files)

Install the dependencies with:
```bash
pip install -r requirements.txt
```

## Customer Dataset Description
Below is a description of the features in the customer dataset:

| **Feature**                    | **Description**                                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------|
| Customer ID                   | Identifier uniquely assigned to each customer, used to distinguish individual customers.             |
| Recency                       | The number of days that have passed since the customer's last purchase.                             |
| Total_Transactions            | The total number of transactions made by the customer.                                              |
| Total_Products_Purchased      | The total quantity of products purchased by the customer across all transactions.                   |
| Total_Spend                   | The total amount of money the customer has spent across all transactions.                           |
| Average_Transaction_Value     | The average value of the customer's transactions, calculated as total spend divided by transactions. |
| Unique_Products_Purchased     | The number of different products the customer has purchased.                                        |
| Cancellation_Frequency        | The total number of transactions that the customer has canceled.                                    |
| Cancellation_Rate             | The proportion of transactions that the customer has canceled, calculated as cancellations/total.   |
| Monthly_Spending_Mean         | The average monthly spending of the customer.                                                       |
| Monthly_Spending_Std          | The standard deviation of the customer's monthly spending, indicating variability.                  |