from mlflow.server.auth.client import AuthServiceClient

tracking_uri = "http://localhost:5000/"

client = AuthServiceClient("tracking_uri")
client.create_user("admin", "admin")
ep = client.create_experiment_permission("myexperiment", "newuser", "READ")
print(f"experiment_id: {ep.experiment_id}")
print(f"user_id: {ep.user_id}")
print(f"permission: {ep.permission}")