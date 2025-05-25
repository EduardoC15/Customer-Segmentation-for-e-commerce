# Customer RFM Segmentation for E-Commerce

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
   - Handled cancelled transactions (2.21% of the total) adding the Transaction_Status column.
   - Cleaned the `Description` column by removing rows containing service descriptions to focus solely on product transactions.
   - Corrected inconsistencies where multiple `StockCode` were associated with a single description and vice versa.
   - Treated zero unit prices by removing or correcting entries to avoid distortions in the analysis.
   - Adding Total_Spend column.

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

3. **Outlier Detection**:
   - Identified outliers in key features such as 'Recency', 'Total_Transactions' and 'Total_Spend' using IsolationForest.
   - IsolationForest detected as Outliers the most important customers, due the importance of these customers, we maintain them.

4. **Correlation Analysis**:
   - Analyzed correlations between features to understand relationships and inform feature selection.
   - Features with high correlation were evaluated to avoid redundancy in the clustering process.

5. **Scaling the Data**:
   - Applied standardization (StandardScaler) to the features to ensure equal weighting in the clustering algorithm.

6. **Determining the Optimal Number of Clusters**:
   - Used methods such as the Elbow Method, Silhouette Score, and Gap Statistic to determine the optimal number of clusters for KMeans.
   - The optimal number was chosen based on the point where adding more clusters yielded diminishing returns in terms of variance explained.

7. **Clustering**:
   - Applied the K-means algorithm to segment customers based on the **Recency**, **Total_Transactions**, and **Total_Spend** columns (RFM features).

8. **Churn Analysis**:
   - Identified churned customers as those with a recency greater than 180 days.
   - Refined the segmentation by labeling churned customers as "Churned [Segment]" to prioritize recovery efforts for high-value lost customers.

9. **Exporting the Cleaned Data**:
   - Exported the cleaned transactional data to `Transactions_cleaned.csv`.
   - Exported the cleaned customer data with engineered features and segmentation labels to `Customer_cleaned.csv`.

## Clustering Results

The clustering analysis identified four main customer segments based on RFM values:

- **Champion (0.25%)**: Customers with very recent activity, high frequency, and the highest total spend. Although this group is the smallest, it is the most valuable. They should be prioritized with personalized rewards and premium services to maintain their loyalty.
- **Loyal (4.70%)**: Active and frequent buyers who demonstrate strong engagement. Representing a stable segment, they are excellent candidates for loyalty programs, exclusive offers, and upselling strategies.
- **Regular (70.40%)**: The core customer base, exhibiting moderate frequency and spending. While consistent, they hold significant potential to be nurtured into higher-value segments.
- **Passenger (4.86%)**: Customers with high recency and low engagement. Though still active, they are at risk of churning and could benefit from low-effort re-engagement initiatives.

### Evaluation Metrics

- **Silhouette Score (0.6758):** A value close to 0.68 suggests well-defined clusters with good cohesion and separation. This indicates a reliable clustering structure.
- **Calinski-Harabasz Score (3732.48):** A high score, reinforcing that the clusters are dense and well-separated.
- **Davies-Bouldin Score (0.7267):** A relatively low value, confirming that clusters are distinct and not overlapping excessively.

## Churn Analysis

To enhance the segmentation, customers with **recency > 180 days** were labeled as **churned**. This provides a clearer picture of at-risk and inactive customers.

### **Updated Segmentation with Churn Labels:**

- **Churned Passenger (19.74%)**: A large group of previously low-value customers who are now inactive. This segment represents a key opportunity for win-back campaigns and reactivation offers.
- **Passenger (4.86%)**: Low-frequency, low-value customers who are still active. They are at risk of churning and require light-touch engagement.
- **Regular (70.40%)**: The most stable and reliable segment. These customers maintain regular activity and should be continuously supported and monitored for changes in behavior.
- **Loyal (4.70%)**: High-frequency customers with recent activity. This group should be nurtured to maintain their loyalty and increase their lifetime value.
- **Churned Loyal (0.05%)**: A very small but valuable group that has recently disengaged. Targeted win-back efforts may be particularly effective given their previous engagement and value.
- **Champion (0.25%)**: The top-tier customers who spend the most and engage frequently. Even though no churn was detected in this group, continued personalized attention is crucial to avoid future losses.

Incorporating churn status into the RFM-based clustering model provides a richer understanding of customer dynamics. This refined segmentation enables the business to:
- Identify high-priority reactivation targets.
- Focus retention strategies on at-risk but valuable customers.
- Maximize the value of active segments through tailored engagement.

## Customer Dataset Description
Below is a description of the features in the customer dataset:

| **Feature**                    | **Description**                                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------|
| **Customer ID**                | Identifier uniquely assigned to each customer, used to distinguish individual customers.             |
| **Recency**                    | The number of days that have passed since the customer's last purchase.                             |
| **Total_Transactions**         | The total number of transactions made by the customer.                                              |
| **Total_Products_Purchased**   | The total quantity of products purchased by the customer across all transactions.                   |
| **Total_Spend**                | The total amount of money the customer has spent across all transactions.                           |
| **Average_Transaction_Value**  | The average value of the customer's transactions, calculated as total spend divided by transactions. |
| **Unique_Products_Purchased**  | The number of different products the customer has purchased.                                        |
| **Cancellation_Frequency**     | The total number of transactions that the customer has cancelled.                                   |
| **Cancellation_Rate**          | The proportion of transactions that the customer has cancelled, calculated as cancellations/total.  |
| **Monthly_Spending_Mean**      | The average monthly spending of the customer.                                                       |
| **Monthly_Spending_Std**       | The standard deviation of the customer's monthly spending, indicating variability.                  |
| **RFM**                        | The customer segmentation category derived from Recency, Total_Transactions, and Total_Spend, indicating the customer's value and engagement level, such as 'Champion', 'Loyal', 'Regular', or 'Passenger'. This has been refined to integrate churn analysis, classifying customers with a recency greater than 180 days (approximately 6 months) as churned and adding churn-specific labels: Churned + Segment. |

## Exported Files
- `Customer_cleaned.csv`: Contains the cleaned customer dataset with engineered features and segmentation labels.
- `Transactions_cleaned.csv`: Contains the cleaned transactional dataset after preprocessing.

## Conclusions
This project successfully segmented the customer base of a UK-based online retailer using K-means clustering on engineered features derived from transactional data.

The integration of churn analysis (defining churn as recency > 180 days) refined the segmentation, highlighting the importance of recovering high-value churned customers (Churned Champions and Churned Loyals) and preventing further churn in at-risk segments like Regulars. The clustering structure was validated with strong evaluation metrics, ensuring reliable customer profiles.

By leveraging these insights, the business can implement targeted marketing strategies to enhance customer retention, recover valuable lost customers, stabilize the core base, and ultimately increase sales and marketing effectiveness.

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
