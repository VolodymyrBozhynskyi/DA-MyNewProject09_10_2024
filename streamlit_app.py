import pandas as pd
import matplotlib.pyplot as plt
# Завантаження дата-сету з CSV-файлу
df = pd.read_csv("Spotify Most Streamed Songs.csv")
print(df.head(20))
plt.plot(df["in_spotify_playlists"], df["track_name"], color =  "green", marker = "x")
plt.title("Кількість плейлистів для кожного треку на Spotify")
plt.xlabel("Кількість плейлистів")
plt.ylabel("Назва треку")
plt.xticks(rotation = 90)
plt.show()
top_10_songs = df.sort_values(by='streams', ascending=False).head(10)

# Побудова стовпчикової діаграми
plt.figure(figsize=(12, 6))
plt.barh(top_10_songs['track_name'], top_10_songs['streams'], color='skyblue')

# Додавання підписів та заголовка
plt.title('Топ-10 пісень за кількістю стрімів на Spotify')
plt.xlabel('Кількість стрімів')
plt.ylabel('Назва пісні')

# Показ графіка
plt.gca().invert_yaxis()  # Інвертуємо вісь Y для правильного порядку
plt.show()
