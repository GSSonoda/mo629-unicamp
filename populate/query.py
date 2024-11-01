from core.core import client
import matplotlib.pyplot as plt

def plot_temp_data(path='temporary/temperature_variation.png'):
    query = """
            SELECT *
            FROM "temperature"
            WHERE
            "temperature" IS NOT NULL
            LIMIT 6
            """
    table = client.query(query=query, database="temp_data", language='sql')
    df = table.to_pandas().sort_values(by="time")
    plt.figure(figsize=(12, 6))
    plt.plot(df['time'], df['temperature'], marker='o', color='b', linestyle='-')
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
            SELECT *
            FROM "temperature"
            ORDER BY time DESC
            LIMIT 1;
            """
    table = client.query(query=query, database="temp_data", language='sql')
    return table.to_pandas().sort_values(by="time")