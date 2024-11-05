from core.core import client, database
import matplotlib.pyplot as plt


def plot_temp_data(longitude='222222', path="temporary/temperature_variation.png"):
    query = f"""
            SELECT *
            FROM "temperature"
            WHERE
            "longitute" IN ({longitude})
            """
    table = client.query(query=query, database=database, language="sql")
    df = table.to_pandas().sort_values(by="time")
    plt.figure(figsize=(12, 6))
    plt.plot(df["time"], df["temperature"], marker="o", color="b", linestyle="-")
    plt.title("Variação de Temperatura ao Longo do Tempo")
    plt.xlabel("Tempo")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path)
    return path


def query_last():
    query = """
                SELECT 
                        DISTINCT ON (latitude, longitude) 
                        longitude, 
                        latitude, 
                        time,
                        temperature
                FROM temperature
                ORDER BY latitude, longitude, time DESC;
            """
    table = client.query(query=query, database=database, language="sql")
    return table.to_pandas().sort_values(by="time")
