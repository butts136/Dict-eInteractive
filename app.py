from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'

# Chargement des mots depuis un fichier JSON
def load_words():
    try:
        with open('words.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Sauvegarde des mots dans un fichier JSON
def save_words(words):
    with open('words.json', 'w') as f:
        json.dump(words, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Butts136' and password == '136Butts':
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('login.html', error='Identifiants incorrects')
    return render_template('login.html')

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin'))
    words = load_words()
    if request.method == 'POST':
        if 'add' in request.form:
            new_word = request.form['new_word']
            if new_word:
                words.append(new_word)
                save_words(words)
        elif 'delete' in request.form:
            word_to_delete = request.form.get('word')
            if word_to_delete:
                words.remove(word_to_delete)
                save_words(words)
    words = load_words()
    return render_template('admin.html', words=words)

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST' and 'name' in request.form:
        session['name'] = request.form['name']
        session['word_index'] = 0
        session['mistakes'] = 0
        return redirect(url_for('test'))
    elif 'name' in session:
        words = load_words()
        index = session.get('word_index', 0)
        if index < len(words):
            current_word = words[index]
            if 'user_input' in request.form:
                user_input = request.form['user_input']
                correct_word = words[index]
                if user_input == correct_word:
                    session['word_index'] += 1
                    return redirect(url_for('test'))
                else:
                    session['mistakes'] += 1
                    error = "Erreur dans le mot."
                    return render_template('test.html', word=current_word, error=error,
                                           mistakes=session['mistakes'], total=len(words),
                                           index=index+1)
            return render_template('test.html', word=current_word, mistakes=session['mistakes'],
                                   total=len(words), index=index+1)
        else:
            return render_template('test_complete.html', mistakes=session['mistakes'],
                                   total=len(words))
    return render_template('enter_name.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1010)
