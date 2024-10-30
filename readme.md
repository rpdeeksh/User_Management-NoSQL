Follow the instructions below to configure the project and run the application.

### Prerequisites

- Python 3.x installed on your machine
- MongoDB Atlas account

### Setup Instructions

#### Step 1: Sign Up / Log In to MongoDB Atlas
1. Go to the [MongoDB Atlas website](https://www.mongodb.com/cloud/atlas).
2. Click **Sign Up** to create an account, or **Log In** if you already have one.

#### Step 2: Create a New Project
1. After logging in, navigate to **Projects** in the left sidebar.
2. Click **New Project** and provide a name (e.g., `MyProject`).
3. Click **Next** to create the project.

#### Step 3: Set Up a Cluster
1. In your new project, click **Build a Cluster**.
2. Choose **Shared Clusters** (the free-tier option).
3. Select a **Cloud Provider** and **Region** based on your location.
4. Click **Create Cluster**.

> **Note**: Free clusters are recommended for development. For production, consider upgrading to a paid cluster.

#### Step 4: Configure Database Access
1. Go to **Database Access** in the left sidebar.
2. Click **Add New Database User**.
3. Set a **Username** and **Password** (keep these for later use).
4. Under **Database User Privileges**, choose **Read and write to any database**.
5. Click **Add User**.

#### Step 5: Set Up Network Access
1. Navigate to **Network Access**.
2. Click **Add IP Address**.
3. Select **Allow Access from Anywhere** (for development convenience).
4. Alternatively, add your own IP address for added security.
5. Click **Confirm**.

#### Step 6: Get Your Connection String
1. Once your cluster is ready, go to **Clusters** in the left sidebar.
2. Click **Connect** next to your cluster.
3. Choose **Connect your application**.
4. Select your **Driver** (e.g., Python) and **Version**.
5. Copy the connection string, which should look similar to this:

### Configuration

- Clone this repository to your local machine.
- In the root directory, open the `config.py` file.
- Paste the MongoDB connection string, replacing `<username>` and `<password>` with your database user credentials, and specify the database and collection names:
```python
# config.py
client = MongoClient("your connection string")  
    db = client["Database Name"]  # Database name
    return db["Collection name"]  # Collection name
```
### Install dependencies
```python
pip install -r requirements.txt
```

### Run the Application
```python
python app.py
```
