# DataCapture_and_analysis_of-car_ride

## Problem Statement:

YourOwnCabs (YOC), an on-demand cab booking start-up, is experiencing rapid growth with a rising number of daily rides and users. The existing MySQL-based backend is unable to handle large-scale, complex queries efficiently, making it difficult for business stakeholders to access timely, data-driven insights. Quick analysis of daily, weekly, and monthly bookings, booking patterns by mobile operating systems, average fares, and total tips is essential for strategic decision-making.
Additionally, YOC generates high-volume clickstream data from user interactions within the mobile app, which is critical for understanding user behaviour and improving engagement. This data requires an optimized, scalable storage and processing solution to support seamless analytics without affecting application performance.
The challenge is to design and implement a robust big data architecture that can efficiently manage both booking and clickstream data, ensuring fast, reliable, and scalable analytics to support the company’s growth.

## Proposed Solution:
To address the growing data and analytics needs of YourOwnCabs (YOC), a scalable big data pipeline is proposed to efficiently manage both booking and clickstream data.

Booking Data Analytics Solution
•	Ingestion: Use Sqoop to import booking data from MySQL to HDFS in scheduled batches.
•	Storage: Save data in Parquet format for optimized storage and fast querying.
•	Processing: Use Apache Spark for data cleaning, aggregations (daily, weekly, monthly counts, OS-wise bookings, average fare, total tips), and reporting.
•	Access: Create Hive external tables for easy querying and integration with BI tools.

Clickstream Data Analytics Solution
•	Ingestion: Use Apache Kafka for real-time clickstream data ingestion.
•	Storage: Store clickstream data in HDFS (Parquet format) for efficient handling.
•	Processing: Apply Spark Structured Streaming for real-time parsing and user behavior tracking.
•	Access: Expose data via Hive tables to support user analytics and engagement strategies.
This solution ensures fast, scalable, and reliable analytics without impacting business operations.


## Data:

The following data will be used for this problem:
•	bookings (The booking data is added to/updated in this table after a booking/ride is successfully completed.) 
  o	booking_id: Booking ID String
  o	customer_id: Customer ID Number
  o	driver_id: Driver ID Number
  o	customer_app_version: Customer App Version String
  o	customer_phone_os_version: Customer mobile operating system
  o	pickup_lat: Pickup latitude
  o	pickup_lon: Pickup longitude
  o	drop_lat: Dropoff latitude
  o	drop_lon: Dropoff longitude
  o	pickup_timestamp: Timestamp at which customer was picked up
  o	drop_timestamp: Timestamp at which customer was dropped at destination
  o	trip_fare: Total amount of the trip
  o	tip_amount: Tip amount given by customer to driver for this ride
  o	currency_code: Currency Code String for the amount paid by customer
  o	cab_color: Color of the cab
  o	cab_registration_no: Registration number string of the vehicle
  o	customer_rating_by_driver: Rating number given by driver to customer after ride
  o	rating_by_customer: Rating number given by customer to driver after ride
  o	passenger_count: Total count of passengers who boarded the cab for ride

•	clickstream (All user’s activity data such as click and page load):
  o	customer_id: Customer ID Number
  o	app_version: Customer App Version String
  o	os_version: User mobile operating system
  o	lat: Latitude
  o	lon: Longitude
  o	page_id: UUID of the page/screen browsed by a user
  o	button_id: UUID of the button clicked by a user
  o	is_button_click: Yes/No depending on whether a user clicked button
  o	is_page_view: Yes/No depending on whether a user loaded a new screen/page
  o	is_scroll_up: Yes/No depending on whether a user scrolled up on the current screen
  o	is_scroll_down: Yes/No depending on whether a user scrolled down on the current screen
  o	timestamp: Timestamp at which the user action is captured

