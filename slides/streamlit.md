# Streamlit


Streamlit er et open-source Python bibliotek, der gør det nemt at bygge og dele data apps. Det er designet til at være hurtigt og intuitivt, hvilket gør det muligt for udviklere at skabe interaktive webapplikationer med minimal indsats.

---

# Installation

For at komme i gang med Streamlit, skal du først installere det. Dette kan gøres ved at køre følgende pip-kommando:

```bash
pip install streamlit
```

---

# Kom godt i gang

Når du har installeret Streamlit, kan du begynde at bygge din første app. Opret en ny Python-fil, f.eks. `app.py`, og tilføj følgende kode:

```python
import streamlit as st

st.title("Min første Streamlit app")
st.write("Hej, verden!")
```
---

# Kør din app

For at køre din app, skal du åbne en terminal, navigere til mappen, hvor din `app.py` fil er gemt, og køre følgende kommando:

```bash
streamlit run app.py
```

Dette vil starte en lokal server, og du kan se din app i din webbrowser på `http://localhost:8501`.

---

# Knapper

Streamlit giver dig mulighed for at tilføje knapper til din app for at gøre den mere interaktiv. Du kan bruge `st.button` til at oprette en knap. Her er et eksempel:

```python
import streamlit as st

st.title("Min første Streamlit app")

if st.button("Klik på mig"):
    st.write("Knappen blev klikket!")
```
---

# Flere knapper

Du kan tilføje flere knapper og håndtere deres klik separat. Her er et eksempel med to knapper:

```python
import streamlit as st

st.title("Min første Streamlit app")

if st.button("Klik på mig"):
    st.write("Knappen blev klikket!")

if st.button("Klik på mig igen"):
    st.write("Den anden knap blev klikket!")

```
---

# Tekstbokse

Streamlit giver dig mulighed for at tilføje tekstbokse til din app, så brugerne kan indtaste oplysninger. Du kan bruge `st.text_input` til at oprette en tekstboks. Her er et eksempel:

```python
import streamlit as st

st.title("Min første Streamlit app")

navn = st.text_input("Indtast dit navn:")
st.write("Hej, ", navn)
```

---

# Flere tekstbokse

Streamlit giver dig mulighed for at tilføje flere tekstbokse til din app. Her er et eksempel med to tekstbokse:

```python
import streamlit as st

st.title("Min første Streamlit app")

for i in range(2):
    navn = st.text_input(f"Indtast dit navn {i + 1}:")
    st.write("Hej, ", navn)
```

---

# Flere sider

Streamlit giver dig mulighed for at oprette flere sider i din app. Du kan bruge `st.sidebar` til at tilføje en sidebjælke, hvor brugerne kan navigere mellem forskellige sider. Her er et eksempel:

```python
import streamlit as st

st.title("Min første Streamlit app")

side = st.sidebar.selectbox("Vælg en side:", ["Forside", "Om os", "Kontakt"])

if side == "Forside":
    st.write("Velkommen til forsiden!")
elif side == "Om os":
    st.write("Her er lidt information om os.")

```

---

# Omdiriger til en anden side

Du kan også omdirigere brugeren til en anden side, når de klikker på en knap. Her er et eksempel:

```python
import streamlit as st

st.title("Min første Streamlit app")

if st.button("Gå til Om os"):
    st.sidebar.selectbox("Vælg en side:", ["Forside", "Om os", "Kontakt"], index=1)

```

---

# Andre widgets

Der findes mange andre widgets i Streamlit, som du kan bruge til at forbedre din app. Her er nogle eksempler:

- `st.checkbox`: Opretter en afkrydsningsboks.
- `st.radio`: Opretter en radioknapgruppe.
- `st.selectbox`: Opretter en dropdown-menu.
- `st.slider`: Opretter en skyder til at vælge værdier.

---

# Checkbox


```python
import streamlit as st

st.title("Min første Streamlit app")

if st.checkbox("Vis besked"):
    st.write("Besked vist!")

```

---

# Radioknapper

```python
import streamlit as st

st.title("Min første Streamlit app")

valg = st.radio("Vælg en mulighed:", ["Mulighed 1", "Mulighed 2", "Mulighed 3"])
st.write("Du valgte:", valg)
```

---

# Slider

```python
import streamlit as st

st.title("Min første Streamlit app")

nummer = st.slider("Vælg et nummer:", 0, 100, 50)
st.write("Du valgte nummeret:", nummer)
```

---

# Selectbox

```python
import streamlit as st

st.title("Min første Streamlit app")

valg = st.selectbox("Vælg en mulighed:", ["Mulighed 1", "Mulighed 2", "Mulighed 3"])
st.write("Du valgte:", valg)
```

---

# Lister

```python
import streamlit as st

st.title("Min første Streamlit app")

liste = ["Element 1", "Element 2", "Element 3"]
valgt_element = st.selectbox("Vælg et element fra listen:", liste)
st.write("Du valgte:", valgt_element)
```

---

 
