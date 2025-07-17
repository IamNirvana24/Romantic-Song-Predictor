from sklearn.linear_model import LogisticRegression

Song_Data = [
    [80, 40],   # Jaadu Teri Nazar
    [75, 35],   # Pehla Nasha
    [68, 30],   # Main Yahaan Hoon
    [120, 70],  # Mitwa
    [130, 90],  # Malhari
    [110, 85],  # Zinda
]

labels = [1,1,1,0,0,0]


model = LogisticRegression()
model.fit(Song_Data, labels)


tempo_energy = [[75,40]]

prediction = model.predict(tempo_energy)

if prediction[0]==1:
    print("🎵 This song is predicted to be Romantic 💖")
else:
    print("🎵 This song is predicted to be Not Romantic ❌")