# 📚 Documentation Frython

> Documentation complète du langage de programmation Frython — Python en français 🐓

---

## Table des matières

1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
3. [Utilisation](#3-utilisation)
4. [Syntaxe complète](#4-syntaxe-complète)
5. [Mots-clés](#5-mots-clés)
6. [Fonctions intégrées](#6-fonctions-intégrées)
7. [Méthodes](#7-méthodes)
8. [Modules traduits](#8-modules-traduits)
9. [Exceptions et erreurs](#9-exceptions-et-erreurs)
10. [Exemples complets](#10-exemples-complets)
11. [API Python](#11-api-python)
12. [Architecture interne](#12-architecture-interne)
13. [Extension VS Code](#13-extension-vs-code)
14. [FAQ](#14-faq)
15. [Contribuer](#15-contribuer)

---

## 1. Introduction

**Frython** est un langage de programmation transpilé basé sur Python. Il permet d'écrire du code Python en utilisant des mots-clés et des fonctions entièrement en français.

### Comment ça fonctionne

```
Code Frython (.fy)
       ↓
  [TRANSPILEUR]
       ↓
  Code Python valide
       ↓
  [INTERPRÉTEUR Python]
       ↓
     Résultat
```

Frython ne réinvente pas la roue — il traduit simplement le code français vers Python standard, puis laisse Python faire le reste. Tout ce que Python peut faire, Frython peut le faire.

### Pourquoi Frython ?

- 🎭 C'est un projet humoristique mais entièrement fonctionnel
- 🎓 Excellent pour apprendre la programmation en français
- 🔧 100% compatible avec toutes les bibliothèques Python
- 🐓 Le coq est une mascotte parfaite

---

## 2. Installation

### Prérequis

- Python 3.8 ou supérieur
- pip

### Depuis PyPI (recommandé)

```bash
pip install frython
```

### Depuis les sources

```bash
git clone https://github.com/Artleboss2/frython.git
cd frython
pip install .
```

### Vérifier l'installation

```bash
python -m frython --version
# Frython 1.0.0 — Python en français 🐓
```

### Sur Windows avec plusieurs versions de Python

Si vous avez plusieurs versions de Python installées :

```bash
C:\Python314\python.exe -m frython mon_fichier.fy
```

Ou créez un alias PowerShell permanent :

```powershell
# Dans votre $PROFILE PowerShell
function frython { C:\Python314\python.exe -m frython $args }
```

---

## 3. Utilisation

### Exécuter un fichier

```bash
python -m frython mon_programme.fy
```

### REPL interactive

```bash
python -m frython
```

```
🐓 Frython v1.0.0 — Python en français, sacré bleu !

🐓 >>> afficher("Bonjour!")
Bonjour!
🐓 >>> x = 42
🐓 >>> x * 2
84
🐓 >>> quitter()
Au revoir! 👋
```

### Options de la ligne de commande

| Option | Description |
|--------|-------------|
| `python -m frython fichier.fy` | Exécuter un fichier |
| `python -m frython` | Lancer la REPL |
| `python -m frython -t fichier.fy` | Afficher le code Python transpilé |
| `python -m frython -v fichier.fy` | Mode verbeux |
| `python -m frython -c "code"` | Exécuter du code direct |
| `python -m frython --mots-cles` | Lister tous les mots-clés |
| `python -m frython --version` | Afficher la version |

### Voir le code Python généré

```bash
python -m frython -t mon_programme.fy
```

Utile pour déboguer ou comprendre comment Frython transpile votre code.

---

## 4. Syntaxe complète

### Variables et types

```python
# Entiers
age = 25
annee = 2026

# Décimaux
taille = 1.75
pi = 3.14159

# Chaînes
prenom = "Marie"
message = 'Bonjour le monde!'
multiligne = """
Ceci est un texte
sur plusieurs lignes
"""

# f-strings
afficher(f"Bonjour, {prenom}! Tu as {age} ans.")

# Booléens
est_majeur = Vrai
est_mineur = Faux

# Nul
valeur = Rien
```

### Structures de données

```python
# Listes
nombres = [1, 2, 3, 4, 5]
mixte = ["texte", 42, Vrai, Rien]

# Dictionnaires
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}

# Ensembles
couleurs = {"rouge", "vert", "bleu"}

# Tuples
coordonnees = (48.8566, 2.3522)
```

### Conditions

```python
# Si simple
si age >= 18:
    afficher("Majeur")

# Si / Sinon
si temperature > 30:
    afficher("Il fait chaud!")
sinon:
    afficher("Il fait frais.")

# Si / Sinonsi / Sinon
si note >= 16:
    mention = "Très bien"
sinonsi note >= 14:
    mention = "Bien"
sinonsi note >= 12:
    mention = "Assez bien"
sinonsi note >= 10:
    mention = "Passable"
sinon:
    mention = "Insuffisant"
```

### Boucles

```python
# Boucle pour
pour i dans intervalle(5):
    afficher(i)

# Boucle pour avec liste
fruits = ["pomme", "banane", "cerise"]
pour fruit dans fruits:
    afficher(fruit)

# Boucle pour avec enumerer
pour i, fruit dans enumerer(fruits):
    afficher(f"{i}: {fruit}")

# Boucle tantque
compteur = 0
tantque compteur < 10:
    afficher(compteur)
    compteur += 1

# Casser et continuer
pour i dans intervalle(10):
    si i == 5:
        casser
    si i % 2 == 0:
        continuer
    afficher(i)
```

### Fonctions

```python
# Fonction simple
déf saluer(nom):
    afficher(f"Bonjour, {nom}!")

# Fonction avec retour
déf additionner(a, b):
    retourner a + b

# Valeurs par défaut
déf saluer(nom, salutation="Bonjour"):
    retourner f"{salutation}, {nom}!"

# *args et **kwargs
déf afficher_tout(*args, **kwargs):
    pour arg dans args:
        afficher(arg)
    pour cle, valeur dans kwargs.elements():
        afficher(f"{cle}: {valeur}")

# Fonction récursive
déf factorielle(n):
    si n <= 1:
        retourner 1
    retourner n * factorielle(n - 1)

# Lambda
doubler = lambda x: x * 2
```

### Classes

```python
classe Animal:
    """Classe de base pour les animaux."""
    
    def __init__(soi, nom, age):
        soi.nom = nom
        soi.age = age
    
    déf parler(soi):
        retourner "..."
    
    déf __str__(soi):
        retourner f"{soi.nom} ({soi.age} ans)"


classe Chien(Animal):
    """Un chien."""
    
    def __init__(soi, nom, age, race):
        super().__init__(nom, age)
        soi.race = race
    
    déf parler(soi):
        retourner "Ouaf!"


# Utilisation
rex = Chien("Rex", 3, "Berger")
afficher(rex)          # Rex (3 ans)
afficher(rex.parler()) # Ouaf!
```

### Compréhensions

```python
# Compréhension de liste
carres = [x**2 pour x dans intervalle(1, 11)]

# Avec condition
pairs = [x pour x dans intervalle(20) si x % 2 == 0]

# Compréhension de dictionnaire
carres_dict = {n: n**2 pour n dans intervalle(1, 6)}

# Compréhension d'ensemble
lettres = {c pour c dans "frython" si c != "o"}
```

### Exceptions

```python
essayer:
    resultat = 10 / 0
sauf ZeroDivisionError:
    afficher("Division par zéro!")
sauf (ValueError, TypeError) comme e:
    afficher(f"Erreur: {e}")
enfin:
    afficher("Toujours exécuté.")

# Lever une exception
déf diviser(a, b):
    si b == 0:
        lever ErreurValeur("Le diviseur ne peut pas être zéro!")
    retourner a / b
```

### Générateurs

```python
déf compter(n):
    i = 0
    tantque i < n:
        rendement i
        i += 1

pour nombre dans compter(5):
    afficher(nombre)
```

### Gestionnaires de contexte

```python
avec ouvrir("fichier.txt", "r") comme f:
    contenu = f.lire()
    afficher(contenu)
```

### Décorateurs

```python
importer functools

déf minuteur(fonction):
    @functools.wraps(fonction)
    déf enveloppe(*args, **kwargs):
        importer time
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        afficher(f"Durée: {time.time() - debut:.3f}s")
        retourner resultat
    retourner enveloppe

@minuteur
déf calcul_lent():
    retourner somme(intervalle(1000000))
```

---

<!-- MOTS_CLES_START -->

### Mots-clés et fonctions intégrées

| Frython | Python |
|---------|--------|
| `Avertissement` | `Warning` |
| `AvertissementDepreciation` | `DeprecationWarning` |
| `AvertissementFutur` | `FutureWarning` |
| `AvertissementRuntime` | `RuntimeWarning` |
| `AvertissementSyntaxe` | `SyntaxWarning` |
| `AvertissementUtilisateur` | `UserWarning` |
| `Ellipsis` | `Ellipsis` |
| `ErreurArret` | `StopIteration` |
| `ErreurAssertion` | `AssertionError` |
| `ErreurAttribut` | `AttributeError` |
| `ErreurCle` | `KeyError` |
| `ErreurConnexion` | `ConnectionError` |
| `ErreurDebordement` | `OverflowError` |
| `ErreurDivisionZero` | `ZeroDivisionError` |
| `ErreurES` | `IOError` |
| `ErreurFichier` | `FileNotFoundError` |
| `ErreurImport` | `ImportError` |
| `ErreurIndentation` | `IndentationError` |
| `ErreurIndex` | `IndexError` |
| `ErreurInterruption` | `KeyboardInterrupt` |
| `ErreurMemoire` | `MemoryError` |
| `ErreurNom` | `NameError` |
| `ErreurNotImplemented` | `NotImplementedError` |
| `ErreurOS` | `OSError` |
| `ErreurPermission` | `PermissionError` |
| `ErreurRecursion` | `RecursionError` |
| `ErreurRuntime` | `RuntimeError` |
| `ErreurSyntaxe` | `SyntaxError` |
| `ErreurSysteme` | `SystemError` |
| `ErreurTabulation` | `TabError` |
| `ErreurTimeout` | `TimeoutError` |
| `ErreurType` | `TypeError` |
| `ErreurUnicode` | `UnicodeError` |
| `ErreurValeur` | `ValueError` |
| `Faux` | `False` |
| `NotImplemented` | `NotImplemented` |
| `Rien` | `None` |
| `Vive la france` | `print(` |
| `Vrai` | `True` |
| `__construire_classe__` | `NATIVE.__build_class__` |
| `__importer__` | `NATIVE.__import__` |
| `a_attribut` | `hasattr` |
| `abc._enregistrer` | `abc._abc_register` |
| `abc._initialisation_interne` | `abc._abc_init` |
| `abc._obtenir_decharge` | `abc._get_dump` |
| `abc._reinitialiser_caches` | `abc._reset_caches` |
| `abc._reinitialiser_registre` | `abc._reset_registry` |
| `abc._verifier_instance` | `abc._abc_instancecheck` |
| `abc._verifier_sous_classe` | `abc._abc_subclasscheck` |
| `abc.actualiser_methodes_abstraites` | `abc.update_abstractmethods` |
| `abc.enregistrer` | `abc._abc_register` |
| `abc.initialisation_interne` | `abc._abc_init` |
| `abc.methode_abstraite` | `abc.abstractmethod` |
| `abc.obtenir_decharge` | `abc._get_dump` |
| `abc.obtenir_jeton_cache` | `abc.get_cache_token` |
| `abc.reinitialiser_caches` | `abc._reset_caches` |
| `abc.reinitialiser_registre` | `abc._reset_registry` |
| `abc.verifier_instance` | `abc._abc_instancecheck` |
| `abc.verifier_sous_classe` | `abc._abc_subclasscheck` |
| `abs` | `NATIVE.abs` |
| `absolu` | `abs` |
| `accumulateur` | `NATIVE.flywheel` |
| `afficher` | `print` |
| `afficher_format` | `format` |
| `afficher_pile` | `NATIVE.printStack` |
| `afficher_pile_inverse` | `NATIVE.printReverseStack` |
| `afficher_pile_verbeuse` | `NATIVE.printVerboseStack` |
| `affirmer` | `assert` |
| `aide` | `help` |
| `aiter` | `NATIVE.aiter` |
| `ajouterStr` | `NATIVE.appendStr` |
| `anext` | `NATIVE.anext` |
| `antigravite.hachage_geo` | `antigravity.geohash` |
| `anyio.attendre_lisible` | `anyio.wait_readable` |
| `anyio.attendre_scriptible` | `anyio.wait_writable` |
| `anyio.connecter_tcp` | `anyio.connect_tcp` |
| `anyio.connecter_unix` | `anyio.connect_unix` |
| `anyio.continuer_apres` | `anyio.move_on_after` |
| `anyio.creer_ecouteur_tcp` | `anyio.create_tcp_listener` |
| `anyio.creer_ecouteur_unix` | `anyio.create_unix_listener` |
| `anyio.creer_fichier_temp` | `anyio.mkstemp` |
| `anyio.creer_groupe_taches` | `anyio.create_task_group` |
| `anyio.creer_repertoire_temp` | `anyio.mkdtemp` |
| `anyio.creer_socket_udp` | `anyio.create_udp_socket` |
| `anyio.creer_socket_udp_connecte` | `anyio.create_connected_udp_socket` |
| `anyio.deadline_actuelle` | `anyio.current_effective_deadline` |
| `anyio.dormir` | `anyio.sleep` |
| `anyio.dormir_jusqua` | `anyio.sleep_until` |
| `anyio.dormir_toujours` | `anyio.sleep_forever` |
| `anyio.echouer_apres` | `anyio.fail_after` |
| `anyio.envelopper_fichier` | `anyio.wrap_file` |
| `anyio.fermer_de_force` | `anyio.aclose_forcefully` |
| `anyio.lancer` | `anyio.run` |
| `anyio.lancer_processus` | `anyio.run_process` |
| `anyio.notifier_fermeture` | `anyio.notify_closing` |
| `anyio.obtenir_moteurs_disponibles` | `anyio.get_available_backends` |
| `anyio.obtenir_repertoire_temp` | `anyio.gettempdir` |
| `anyio.obtenir_tache_actuelle` | `anyio.get_current_task` |
| `anyio.obtenir_taches_en_cours` | `anyio.get_running_tasks` |
| `anyio.obtenir_tous_les_moteurs` | `anyio.get_all_backends` |
| `anyio.ouvrir_fichier` | `anyio.open_file` |
| `anyio.ouvrir_processus` | `anyio.open_process` |
| `anyio.temps_actuel` | `anyio.current_time` |
| `appelable` | `NATIVE.callable` |
| `appeler` | `callable` |
| `appendStr` | `NATIVE.appendStr` |
| `arguments._copier_elements` | `argparse._copy_items` |
| `arguments._nom_programme` | `argparse._prog_name` |
| `arguments._obtenir_nom_action` | `argparse._get_action_name` |
| `arguments.copier_elements` | `argparse._copy_items` |
| `arguments.n_obtenir_texte` | `argparse.ngettext` |
| `arguments.nom_programme` | `argparse._prog_name` |
| `arguments.obtenir_nom_action` | `argparse._get_action_name` |
| `arrondir` | `round` |
| `ascii` | `NATIVE.ascii` |
| `ast._definir_dims` | `ast._dims_setter` |
| `ast._diviser_lignes_sans_ff` | `ast._splitlines_no_ff` |
| `ast._obtenir_dims` | `ast._dims_getter` |
| `ast._remplir_espaces` | `ast._pad_whitespace` |
| `ast.analyser` | `ast.parse` |
| `ast.comparer` | `ast.compare` |
| `ast.copier_emplacement` | `ast.copy_location` |
| `ast.corriger_emplacements` | `ast.fix_missing_locations` |
| `ast.decharger` | `ast.dump` |
| `ast.definir_dims` | `ast._dims_setter` |
| `ast.desanalyser` | `ast.unparse` |
| `ast.diviser_lignes_sans_ff` | `ast._splitlines_no_ff` |
| `ast.evaluer_litteral` | `ast.literal_eval` |
| `ast.incrementer_ligne` | `ast.increment_lineno` |
| `ast.iterer_champs` | `ast.iter_fields` |
| `ast.iterer_noeuds_enfants` | `ast.iter_child_nodes` |
| `ast.obtenir_dims` | `ast._dims_getter` |
| `ast.obtenir_docstring` | `ast.get_docstring` |
| `ast.obtenir_segment_source` | `ast.get_source_segment` |
| `ast.parcourir` | `ast.walk` |
| `ast.remplir_espaces` | `ast._pad_whitespace` |
| `asuivant` | `NATIVE.anext` |
| `asynchrone` | `async` |
| `asyncio._desenregistrer_tache` | `asyncio._unregister_task` |
| `asyncio._enregistrer_tache` | `asyncio._register_task` |
| `asyncio._entrer_dans_tache` | `asyncio._enter_task` |
| `asyncio._quitter_tache` | `asyncio._leave_task` |
| `asyncio.assurer_futur` | `asyncio.ensure_future` |
| `asyncio.attendre` | `asyncio.wait` |
| `asyncio.attendre_pendant` | `asyncio.wait_for` |
| `asyncio.au_fur_et_a_mesure` | `asyncio.as_completed` |
| `asyncio.bouclier` | `asyncio.shield` |
| `asyncio.creer_sous_processus_exec` | `asyncio.create_subprocess_exec` |
| `asyncio.creer_sous_processus_shell` | `asyncio.create_subprocess_shell` |
| `asyncio.creer_tache` | `asyncio.create_task` |
| `asyncio.definir_boucle` | `asyncio.set_event_loop` |
| `asyncio.delai_limite` | `asyncio.timeout` |
| `asyncio.delai_limite_a` | `asyncio.timeout_at` |
| `asyncio.demarrer_serveur` | `asyncio.start_server` |
| `asyncio.desenregistrer_tache` | `asyncio._unregister_task` |
| `asyncio.dormir` | `asyncio.sleep` |
| `asyncio.enregistrer_tache` | `asyncio._register_task` |
| `asyncio.entrer_dans_tache` | `asyncio._enter_task` |
| `asyncio.envelopper_futur` | `asyncio.wrap_future` |
| `asyncio.est_coroutine` | `asyncio.iscoroutine` |
| `asyncio.est_fonction_coroutine` | `asyncio.iscoroutinefunction` |
| `asyncio.est_futur` | `asyncio.isfuture` |
| `asyncio.lancer` | `asyncio.run` |
| `asyncio.lancer_coroutine_filetée` | `asyncio.run_coroutine_threadsafe` |
| `asyncio.nouvelle_boucle` | `asyncio.new_event_loop` |
| `asyncio.obtenir_boucle` | `asyncio.get_event_loop` |
| `asyncio.obtenir_boucle_actuelle` | `asyncio.get_running_loop` |
| `asyncio.ouvrir_connexion` | `asyncio.open_connection` |
| `asyncio.quitter_tache` | `asyncio._leave_task` |
| `asyncio.rassembler` | `asyncio.gather` |
| `asyncio.tache_actuelle` | `asyncio.current_task` |
| `asyncio.toutes_les_taches` | `asyncio.all_tasks` |
| `asyncio.vers_fil` | `asyncio.to_thread` |
| `attendre` | `await` |
| `attr.a` | `attr.has` |
| `attr.associer` | `attr.assoc` |
| `attr.attribut` | `attr.attrib` |
| `attr.champ` | `attr.field` |
| `attr.champs` | `attr.fields` |
| `attr.comparer_avec` | `attr.cmp_using` |
| `attr.creer_classe` | `attr.make_class` |
| `attr.definir` | `attr.define` |
| `attr.dict_champs` | `attr.fields_dict` |
| `attr.en_dict` | `attr.asdict` |
| `attr.en_tuple` | `attr.astuple` |
| `attr.evoluer` | `attr.evolve` |
| `attr.mutable` | `attr.mutable` |
| `attr.resoudre_types` | `attr.resolve_types` |
| `attr.valider` | `attr.validate` |
| `attrs.a` | `attrs.has` |
| `attrs.associer` | `attrs.assoc` |
| `attrs.champs` | `attrs.fields` |
| `attrs.comparer_avec` | `attrs.cmp_using` |
| `attrs.creer_classe` | `attrs.make_class` |
| `attrs.definir` | `attrs.define` |
| `attrs.dict_champs` | `attrs.fields_dict` |
| `attrs.en_dict` | `attrs.asdict` |
| `attrs.en_tuple` | `attrs.astuple` |
| `attrs.evoluer` | `attrs.evolve` |
| `attrs.field` | `attrs.field` |
| `attrs.inspecter` | `attrs.inspect` |
| `attrs.mutable` | `attrs.mutable` |
| `attrs.resoudre_types` | `attrs.resolve_types` |
| `attrs.valider` | `attrs.validate` |
| `aucun` | `any` |
| `avec` | `with` |
| `base64._octets_depuis_donnees_decodees` | `base64._bytes_from_decode_data` |
| `base64._verification_type_entree` | `base64._input_type_check` |
| `base64.a85_decoder` | `base64.a85decode` |
| `base64.a85_encoder` | `base64.a85encode` |
| `base64.b16_decoder` | `base64.b16decode` |
| `base64.b16_encoder` | `base64.b16encode` |
| `base64.b32_decoder` | `base64.b32decode` |
| `base64.b32_encoder` | `base64.b32encode` |
| `base64.b64_decoder` | `base64.b64decode` |
| `base64.b64_encoder` | `base64.b64encode` |
| `base64.b64_url_decoder` | `base64.urlsafe_b64decode` |
| `base64.b64_url_encoder` | `base64.urlsafe_b64encode` |
| `base64.decoder` | `base64.decode` |
| `base64.decoder_octets` | `base64.decodebytes` |
| `base64.encoder` | `base64.encode` |
| `base64.encoder_octets` | `base64.encodebytes` |
| `base64.octets_depuis_donnees_decodees` | `base64._bytes_from_decode_data` |
| `base64.verification_type_entree` | `base64._input_type_check` |
| `bdb.definir_trace` | `bdb.set_trace` |
| `bdb.gestionnaire_contexte` | `bdb.contextmanager` |
| `bdb.verifier_nom_fonction` | `bdb.checkfuncname` |
| `bin` | `NATIVE.bin` |
| `binaire` | `NATIVE.bin` |
| `bisect.bissection` | `bisect.bisect` |
| `bisect.bissection_droite` | `bisect.bisect_right` |
| `bisect.bissection_gauche` | `bisect.bisect_left` |
| `bisect.insérer_trié` | `bisect.insort` |
| `bisect.insérer_trié_droite` | `bisect.insort_right` |
| `bisect.insérer_trié_gauche` | `bisect.insort_left` |
| `booleen` | `bool` |
| `bound` | `NATIVE.bound` |
| `breakpoint` | `NATIVE.breakpoint` |
| `bs4.convertir` | `bs4.cast` |
| `build.verifier_dependance` | `build.check_dependency` |
| `bz2.compresser` | `bz2.compress` |
| `bz2.decompresser` | `bz2.decompress` |
| `bz2.ouvrir` | `bz2.open` |
| `calendrier._longueur_mois` | `calendar._monthlen` |
| `calendrier._mois_precedent` | `calendar._prevmonth` |
| `calendrier._mois_suivant` | `calendar._nextmonth` |
| `calendrier._valider_mois` | `calendar._validate_month` |
| `calendrier.definir_premier_jour_semaine` | `calendar.setfirstweekday` |
| `calendrier.est_bissextile` | `calendar.isleap` |
| `calendrier.formater` | `calendar.format` |
| `calendrier.jour_semaine` | `calendar.weekday` |
| `calendrier.jours_bissextiles` | `calendar.leapdays` |
| `calendrier.longueur_mois` | `calendar._monthlen` |
| `calendrier.mois_precedent` | `calendar._prevmonth` |
| `calendrier.mois_suivant` | `calendar._nextmonth` |
| `calendrier.plage_mois` | `calendar.monthrange` |
| `calendrier.valider_mois` | `calendar._validate_month` |
| `callable` | `NATIVE.callable` |
| `caractere` | `chr` |
| `casser` | `break` |
| `certains` | `NATIVE.any` |
| `certificats.contenu` | `certifi.contents` |
| `certificats.ou` | `certifi.where` |
| `chaine` | `str` |
| `chr` | `NATIVE.chr` |
| `clamp` | `NATIVE.clamp` |
| `classe` | `class` |
| `classique` | `classmethod` |
| `clic.argument` | `click.argument` |
| `clic.barre_progression` | `click.progressbar` |
| `clic.commande` | `click.command` |
| `clic.confirmer` | `click.confirm` |
| `clic.creer_decorateur_passage` | `click.make_pass_decorator` |
| `clic.demander` | `click.prompt` |
| `clic.echo` | `click.echo` |
| `clic.echo_page` | `click.echo_via_pager` |
| `clic.editer` | `click.edit` |
| `clic.effacer` | `click.clear` |
| `clic.enlever_style` | `click.unstyle` |
| `clic.envelopper_texte` | `click.wrap_text` |
| `clic.formater_nom_fichier` | `click.format_filename` |
| `clic.groupe` | `click.group` |
| `clic.lancer` | `click.launch` |
| `clic.lire_caractere` | `click.getchar` |
| `clic.obtenir_contexte_actuel` | `click.get_current_context` |
| `clic.obtenir_dossier_app` | `click.get_app_dir` |
| `clic.obtenir_flux_binaire` | `click.get_binary_stream` |
| `clic.obtenir_flux_texte` | `click.get_text_stream` |
| `clic.option` | `click.option` |
| `clic.option_aide` | `click.help_option` |
| `clic.option_confirmation` | `click.confirmation_option` |
| `clic.option_mot_de_passe` | `click.password_option` |
| `clic.option_version` | `click.version_option` |
| `clic.ouvrir_fichier` | `click.open_file` |
| `clic.passer_contexte` | `click.pass_context` |
| `clic.passer_objet` | `click.pass_obj` |
| `clic.pause` | `click.pause` |
| `clic.secho` | `click.secho` |
| `clic.style` | `click.style` |
| `code.compiler_commande` | `code.compile_command` |
| `code.interagir` | `code.interact` |
| `codecs.ascii_decoder` | `codecs.ascii_decode` |
| `codecs.ascii_encoder` | `codecs.ascii_encode` |
| `codecs.chercher` | `codecs.lookup` |
| `codecs.chercher_erreur` | `codecs.lookup_error` |
| `codecs.construire_carte_caracteres` | `codecs.charmap_build` |
| `codecs.creer_carte_encodage` | `codecs.make_encoding_map` |
| `codecs.decoder` | `codecs.decode` |
| `codecs.desenregistrer` | `codecs.unregister` |
| `codecs.echappement_decoder` | `codecs.escape_decode` |
| `codecs.echappement_encoder` | `codecs.escape_encode` |
| `codecs.encoder` | `codecs.encode` |
| `codecs.enregistrer` | `codecs.register` |
| `codecs.enregistrer_erreur` | `codecs.register_error` |
| `codecs.erreur_remplacement_barre` | `codecs.backslashreplace_errors` |
| `codecs.erreurs_strictes` | `codecs.strict_errors` |
| `codecs.fichier_encode` | `codecs.EncodedFile` |
| `codecs.ignorer_erreurs` | `codecs.ignore_errors` |
| `codecs.iterer_decoder` | `codecs.iterdecode` |
| `codecs.iterer_encoder` | `codecs.iterencode` |
| `codecs.latin1_decoder` | `codecs.latin_1_decode` |
| `codecs.latin1_encoder` | `codecs.latin_1_encode` |
| `codecs.obtenir_decoder` | `codecs.getdecoder` |
| `codecs.obtenir_ecrivain` | `codecs.getwriter` |
| `codecs.obtenir_encoder` | `codecs.getencoder` |
| `codecs.obtenir_lecteur` | `codecs.getreader` |
| `codecs.ouvrir` | `codecs.open` |
| `codecs.utf8_decoder` | `codecs.utf_8_decode` |
| `codecs.utf8_encoder` | `codecs.utf_8_encode` |
| `codeop._compiler` | `codeop._compile` |
| `codeop._peut_etre_compiler` | `codeop._maybe_compile` |
| `codeop.compiler` | `codeop._compile` |
| `codeop.compiler_commande` | `codeop.compile_command` |
| `codeop.peut_etre_compiler` | `codeop._maybe_compile` |
| `collecte_pstat` | `NATIVE.pstatcollect` |
| `collections._compter_elements` | `collections._count_elements` |
| `collections._est_mot_cle` | `collections._iskeyword` |
| `collections._repr_recursif` | `collections._recursive_repr` |
| `collections.compter_elements` | `collections._count_elements` |
| `collections.est_mot_cle` | `collections._iskeyword` |
| `collections.repr_recursif` | `collections._recursive_repr` |
| `collections.tuple_nomme` | `collections.namedtuple` |
| `colorama.desinit` | `colorama.deinit` |
| `colorama.init` | `colorama.init` |
| `colorama.reinit` | `colorama.reinit` |
| `colorama.reparer_console_windows` | `colorama.just_fix_windows_console` |
| `colorama.texte_couleur` | `colorama.colorama_text` |
| `comme` | `as` |
| `comparaison_fichier.comparer` | `filecmp.cmp` |
| `comparaison_fichier.comparer_fichiers` | `filecmp.cmpfiles` |
| `comparaison_fichier.vider_cache` | `filecmp.clear_cache` |
| `compile` | `NATIVE.compile` |
| `compiler` | `NATIVE.compile` |
| `complexe` | `complex` |
| `configIsToday` | `NATIVE.configIsToday` |
| `configurationEstAujourdhui` | `NATIVE.configIsToday` |
| `contexte.envelopper` | `contextlib.wraps` |
| `contexte.gestionnaire` | `contextlib.contextmanager` |
| `contexte.gestionnaire_async` | `contextlib.asynccontextmanager` |
| `continuer` | `continue` |
| `contour.calculer_tailles_blocs` | `contourpy.calc_chunk_sizes` |
| `contour.convertir_lignes` | `contourpy.convert_lines` |
| `contour.convertir_rempli` | `contourpy.convert_filled` |
| `contour.generateur_contour` | `contourpy.contour_generator` |
| `copie._copie_profonde_dict` | `copy._deepcopy_dict` |
| `copie._copie_profonde_liste` | `copy._deepcopy_list` |
| `copie.copie_profonde` | `copy.deepcopy` |
| `copie.copie_profonde_dict` | `copy._deepcopy_dict` |
| `copie.copie_profonde_liste` | `copy._deepcopy_list` |
| `copie.copier` | `copy.copy` |
| `copie.remplacer` | `copy.replace` |
| `correspondance.filtrer` | `fnmatch.filter` |
| `correspondance.fnmatch` | `fnmatch.fnmatch` |
| `correspondance.traduire` | `fnmatch.translate` |
| `couleurs.hls_vers_rgb` | `colorsys.hls_to_rgb` |
| `couleurs.hsv_vers_rgb` | `colorsys.hsv_to_rgb` |
| `couleurs.rgb_vers_hls` | `colorsys.rgb_to_hls` |
| `couleurs.rgb_vers_hsv` | `colorsys.rgb_to_hsv` |
| `creer_liste` | `NATIVE.makeList` |
| `creer_tuple` | `NATIVE.makeTuple` |
| `csv.desenregistrer_dialecte` | `csv.unregister_dialect` |
| `csv.ecrivain` | `csv.writer` |
| `csv.enregistrer_dialecte` | `csv.register_dialect` |
| `csv.lecteur` | `csv.reader` |
| `csv.limite_taille_champ` | `csv.field_size_limit` |
| `csv.lister_dialectes` | `csv.list_dialects` |
| `csv.obtenir_dialecte` | `csv.get_dialect` |
| `ctypes.ErreurFormat` | `ctypes.FormatError` |
| `ctypes.ErreurWin` | `ctypes.WinError` |
| `ctypes.POINTEUR` | `ctypes.POINTER` |
| `ctypes.TABLEAU` | `ctypes.ARRAY` |
| `ctypes._charger_bibliotheque` | `ctypes._LoadLibrary` |
| `ctypes.adresse_de` | `ctypes.addressof` |
| `ctypes.alignement` | `ctypes.alignment` |
| `ctypes.chaine_a` | `ctypes.string_at` |
| `ctypes.chaine_large_a` | `ctypes.wstring_at` |
| `ctypes.charger_bibliotheque` | `ctypes._LoadLibrary` |
| `ctypes.convertir` | `ctypes.cast` |
| `ctypes.creer_tampon_chaine` | `ctypes.create_string_buffer` |
| `ctypes.creer_tampon_unicode` | `ctypes.create_unicode_buffer` |
| `ctypes.obtenir_derniere_erreur` | `ctypes.get_last_error` |
| `ctypes.obtenir_errno` | `ctypes.get_errno` |
| `ctypes.par_ref` | `ctypes.byref` |
| `ctypes.pointeur` | `ctypes.pointer` |
| `ctypes.redimensionner` | `ctypes.resize` |
| `ctypes.taille_de` | `ctypes.sizeof` |
| `ctypes.tampon_c` | `ctypes.c_buffer` |
| `ctypes.vue_memoire_a` | `ctypes.memoryview_at` |
| `cycleur.ajouter` | `cycler.add` |
| `cycleur.concatener` | `cycler.concat` |
| `cycleur.cycleur` | `cycler.cycler` |
| `cycleur.multiplier` | `cycler.mul` |
| `cycleur.reduire` | `cycler.reduce` |
| `dans` | `in` |
| `dbm.ouvrir` | `dbm.open` |
| `dbm.quel_db` | `dbm.whichdb` |
| `de` | `from` |
| `decimal` | `float` |
| `decimal.contexte_local` | `decimal.localcontext` |
| `decimal.definir_contexte` | `decimal.setcontext` |
| `decimal.obtenir_contexte` | `decimal.getcontext` |
| `definir_attribut` | `setattr` |
| `dictionnaire` | `dict` |
| `dictionnaire_histogramme` | `NATIVE.histogramDict` |
| `diff._calculer_ratio` | `difflib._calculate_ratio` |
| `diff.calculer_ratio` | `difflib._calculate_ratio` |
| `diff.diff_contexte` | `difflib.context_diff` |
| `diff.diff_unifie` | `difflib.unified_diff` |
| `diff.obtenir_correspondances_proches` | `difflib.get_close_matches` |
| `diff.restaurer` | `difflib.restore` |
| `dill.charger` | `dill.load` |
| `dill.charger_module` | `dill.load_module` |
| `dill.charger_session` | `dill.load_session` |
| `dill.copier` | `dill.copy` |
| `dill.sauvegarder` | `dill.dump` |
| `dill.sauvegarder_module` | `dill.dump_module` |
| `dill.sauvegarder_session` | `dill.dump_session` |
| `dill.verifier` | `dill.check` |
| `dis._desassembler_octets` | `dis._disassemble_bytes` |
| `dis._trouver_importations` | `dis._find_imports` |
| `dis.analyser` | `dis.dis` |
| `dis.desassembler` | `dis.disassemble` |
| `dis.desassembler_octets` | `dis._disassemble_bytes` |
| `dis.effet_pile` | `dis.stack_effect` |
| `dis.info_code` | `dis.code_info` |
| `dis.instructions` | `dis.get_instructions` |
| `dis.montrer_code` | `dis.show_code` |
| `dis.trouver_importations` | `dis._find_imports` |
| `div_reste` | `NATIVE.divmod` |
| `divmod` | `divmod` |
| `divreste` | `NATIVE.divmod` |
| `django.configuration` | `django.setup` |
| `django.obtenir_version` | `django.get_version` |
| `doctest._indenter` | `doctest._indent` |
| `doctest._tester` | `doctest._test` |
| `doctest.deboguer` | `doctest.debug` |
| `doctest.exemples_vers_script` | `doctest.script_from_examples` |
| `doctest.indenter` | `doctest._indent` |
| `doctest.source_test` | `doctest.testsource` |
| `doctest.tester` | `doctest._test` |
| `doctest.tester_fichier` | `doctest.testfile` |
| `doctest.tester_module` | `doctest.testmod` |
| `donnees._en_dict_interne` | `dataclasses._asdict_inner` |
| `donnees.champ` | `dataclasses.field` |
| `donnees.champs` | `dataclasses.fields` |
| `donnees.creer_donnee_classe` | `dataclasses.make_dataclass` |
| `donnees.donnee_classe` | `dataclasses.dataclass` |
| `donnees.en_dict` | `dataclasses.asdict` |
| `donnees.en_dict_interne` | `dataclasses._asdict_inner` |
| `donnees.en_tuple` | `dataclasses.astuple` |
| `donnees.est_donnee_classe` | `dataclasses.is_dataclass` |
| `donnees.remplacer` | `dataclasses.replace` |
| `déf` | `def` |
| `email.message_depuis_chaine` | `email.message_from_string` |
| `email.message_depuis_fichier` | `email.message_from_file` |
| `email.message_depuis_fichier_binaire` | `email.message_from_binary_file` |
| `email.message_depuis_octets` | `email.message_from_bytes` |
| `encodage.definir_journalisation` | `charset_normalizer.set_logging_handler` |
| `encodage.depuis_chemin` | `charset_normalizer.from_path` |
| `encodage.depuis_octets` | `charset_normalizer.from_bytes` |
| `encodage.detecter` | `charset_normalizer.detect` |
| `encodage.est_binaire` | `charset_normalizer.is_binary` |
| `encodages.normaliser_encodage` | `encodings.normalize_encoding` |
| `encodages.rechercher_fonction` | `encodings.search_function` |
| `enfin` | `finally` |
| `ensemble` | `set` |
| `ensurepip._amorce` | `ensurepip._bootstrap` |
| `ensurepip.amorce` | `ensurepip.bootstrap` |
| `ensurepip.version` | `ensurepip.version` |
| `entier` | `int` |
| `entier_long` | `int` |
| `entree` | `input` |
| `entree_erreur` | `stderr` |
| `entree_fichier.entree` | `fileinput.input` |
| `entree_fichier.fermer` | `fileinput.close` |
| `entree_fichier.fichier_suivant` | `fileinput.nextfile` |
| `entree_fichier.nom_fichier` | `fileinput.filename` |
| `entree_fichier.num_ligne` | `fileinput.lineno` |
| `entree_standard` | `stdin` |
| `enum._est_prive` | `enum._is_private` |
| `enum.afficher_valeurs_drapeau` | `enum.show_flag_values` |
| `enum.est_prive` | `enum._is_private` |
| `enum.unique` | `enum.unique` |
| `enumerer` | `enumerate` |
| `erreur_enregistree` | `NATIVE.exceptionLogged` |
| `essayer` | `try` |
| `est` | `is` |
| `et` | `and` |
| `evaluer` | `eval` |
| `exception_enregistree` | `NATIVE.exceptionLogged` |
| `exception_journalisee` | `NATIVE.exceptionLogged` |
| `executer` | `exec` |
| `executer_fichier` | `execfile` |
| `fermer` | `close` |
| `fige` | `frozenset` |
| `filtrer` | `filter` |
| `flask.apres_cette_requete` | `flask.after_this_request` |
| `flask.avorter` | `flask.abort` |
| `flask.creer_reponse` | `flask.make_response` |
| `flask.envoyer_depuis_dossier` | `flask.send_from_directory` |
| `flask.envoyer_fichier` | `flask.send_file` |
| `flask.flasher` | `flask.flash` |
| `flask.jsonnifier` | `flask.jsonify` |
| `flask.obtenir_messages_flash` | `flask.get_flashed_messages` |
| `flask.rediriger` | `flask.redirect` |
| `flask.rendre_chaine_modele` | `flask.render_template_string` |
| `flask.rendre_modele` | `flask.render_template` |
| `flask.url_pour` | `flask.url_for` |
| `flux.analyser` | `feedparser.parse` |
| `flux.enregistrer_gestionnaire_date` | `feedparser.registerDateHandler` |
| `fonctions._trouver_impl` | `functools._find_impl` |
| `fonctions.cache` | `functools.cache` |
| `fonctions.dispatch_unique` | `functools.singledispatch` |
| `fonctions.envelopper` | `functools.wraps` |
| `fonctions.lru_cache` | `functools.lru_cache` |
| `fonctions.mise_a_jour_enveloppe` | `functools.update_wrapper` |
| `fonctions.ordre_total` | `functools.total_ordering` |
| `fonctions.reduire` | `functools.reduce` |
| `fonctions.trouver_impl` | `functools._find_impl` |
| `fonctions.wraps` | `functools.wraps` |
| `formater` | `NATIVE.format` |
| `formater_chaine` | `format` |
| `fractions._arrondir_exposant` | `fractions._round_to_exponent` |
| `fractions.arrondir_exposant` | `fractions._round_to_exponent` |
| `frython.transpileur` | `frython.transpiler` |
| `fsspec.compressions_disponibles` | `fsspec.available_compressions` |
| `fsspec.enregistrer_implementation` | `fsspec.register_implementation` |
| `fsspec.ouvrir` | `fsspec.open` |
| `fsspec.ouvrir_fichiers` | `fsspec.open_files` |
| `fsspec.protocoles_disponibles` | `fsspec.available_protocols` |
| `fsspec.systeme_fichiers` | `fsspec.filesystem` |
| `functorch.grad` | `functorch.grad` |
| `functorch.hessienne` | `functorch.hessian` |
| `functorch.rendre_fonctionnel` | `functorch.make_functional` |
| `functorch.vmap` | `functorch.vmap` |
| `geler` | `frozenset` |
| `generateur_boucle` | `NATIVE.loopGen` |
| `generateur_nul` | `NATIVE.nullGen` |
| `global` | `global` |
| `globals` | `globals` |
| `hash` | `hash` |
| `hex` | `hex` |
| `identifiant` | `id` |
| `importer` | `import` |
| `importer_module` | `__import__` |
| `imprimer` | `print` |
| `imprimer_erreur` | `sys.stderr.write` |
| `index` | `__index__` |
| `instance_de` | `isinstance` |
| `interpolation_linéaire` | `NATIVE.lerp` |
| `intervalle` | `range` |
| `inverser` | `reversed` |
| `inverser_dictionnaire` | `NATIVE.invertDict` |
| `inverser_dictionnaire_sans_perte` | `NATIVE.invertDictLossless` |
| `iter` | `iter` |
| `jeux_donnees.activer_barre_progression` | `datasets.enable_progress_bar` |
| `jeux_donnees.activer_cache` | `datasets.enable_caching` |
| `jeux_donnees.charger` | `datasets.load_dataset` |
| `jeux_donnees.charger_depuis_disque` | `datasets.load_from_disk` |
| `jeux_donnees.concatener` | `datasets.concatenate_datasets` |
| `jeux_donnees.desactiver_barre_progression` | `datasets.disable_progress_bar` |
| `jeux_donnees.desactiver_cache` | `datasets.disable_caching` |
| `jeux_donnees.entrelacer` | `datasets.interleave_datasets` |
| `journaliser_bloc` | `NATIVE.logBlock` |
| `lambda` | `lambda` |
| `lerp` | `NATIVE.lerp` |
| `lever` | `raise` |
| `lien` | `NATIVE.bound` |
| `limite` | `NATIVE.bound` |
| `liste` | `list` |
| `locals` | `locals` |
| `longueur` | `len` |
| `longueur_max` | `max` |
| `longueur_min` | `min` |
| `mapper` | `map` |
| `maximum` | `max` |
| `memoire` | `memoryview` |
| `minimum` | `min` |
| `n_importe_quel` | `NATIVE.any` |
| `nom_type` | `NATIVE.typeName` |
| `nom_type_securise` | `NATIVE.safeTypeName` |
| `nom_unique` | `NATIVE.uniqueName` |
| `non` | `not` |
| `nonlocal` | `nonlocal` |
| `numero_serie` | `NATIVE.serialNum` |
| `objet` | `object` |
| `obtenir_attribut` | `getattr` |
| `obtenir_base` | `NATIVE.getBase` |
| `obtenir_depot` | `NATIVE.getRepository` |
| `octal` | `oct` |
| `octets` | `bytes` |
| `ordinal` | `ord` |
| `ou` | `or` |
| `ouvrir` | `open` |
| `pasdans` | `not in` |
| `passer` | `pass` |
| `pince` | `NATIVE.clamp` |
| `point_de_rupture` | `NATIVE.breakpoint` |
| `pointderupture` | `NATIVE.breakpoint` |
| `pour` | `for` |
| `prochain` | `next` |
| `prochain_async` | `anext` |
| `profile` | `NATIVE.profiled` |
| `profiler.etiquette` | `cProfile.label` |
| `profiler.lancer` | `cProfile.run` |
| `profiler.lancer_contexte` | `cProfile.runctx` |
| `propriete` | `property` |
| `puissance` | `pow` |
| `rapport` | `NATIVE.report` |
| `registre_copie.ajouter_extension` | `copyreg.add_extension` |
| `registre_copie.constructeur` | `copyreg.constructor` |
| `registre_copie.supprimer_extension` | `copyreg.remove_extension` |
| `regulateur` | `NATIVE.flywheel` |
| `rendement` | `yield` |
| `rep` | `NATIVE.dir` |
| `repertoire` | `dir` |
| `repr` | `repr` |
| `repr_rapide` | `NATIVE.fastRepr` |
| `repr_securise` | `NATIVE.safeRepr` |
| `representation_rapide` | `NATIVE.fastRepr` |
| `reseau.adresse_vers_infos` | `aiohappyeyeballs.addr_to_addr_infos` |
| `reseau.demarrer_connexion` | `aiohappyeyeballs.start_connection` |
| `reseau.extraire_infos_entrelacees` | `aiohappyeyeballs.pop_addr_infos_interleave` |
| `reseau.supprimer_infos_adresse` | `aiohappyeyeballs.remove_addr_infos` |
| `retourner` | `return` |
| `saisir` | `input` |
| `sauf` | `except` |
| `serrer` | `NATIVE.clamp` |
| `si` | `if` |
| `sinon` | `else` |
| `sinonsi` | `elif` |
| `soi` | `self` |
| `somme` | `sum` |
| `sortie_standard` | `stdout` |
| `sous_classe` | `issubclass` |
| `statique` | `staticmethod` |
| `suivant_async` | `NATIVE.anext` |
| `super` | `super` |
| `supprimer` | `del` |
| `supprimer_attribut` | `delattr` |
| `tableau` | `bytearray` |
| `taille` | `sizeof` |
| `tantque` | `while` |
| `tous` | `NATIVE.all` |
| `tout_compiler.compiler_chemin` | `compileall.compile_path` |
| `tout_compiler.compiler_dossier` | `compileall.compile_dir` |
| `tout_compiler.compiler_fichier` | `compileall.compile_file` |
| `toutca` | `any` |
| `tranche` | `slice` |
| `trier` | `sorted` |
| `tuple` | `tuple` |
| `type` | `type` |
| `type._appeler_annoter_interne` | `annotationlib._get_and_call_annotate` |
| `type._constructeur_modele_ast` | `annotationlib._template_to_ast_constructor` |
| `type._construire_cloture` | `annotationlib._build_closure` |
| `type._literal_modele_ast` | `annotationlib._template_to_ast_literal` |
| `type._modele_vers_ast` | `annotationlib._template_to_ast` |
| `type._obtenir_annotations_doubles` | `annotationlib._get_dunder_annotations` |
| `type._reescrire_deballage_etoile` | `annotationlib._rewrite_star_unpack` |
| `type._transformer_en_chaine_unique` | `annotationlib._stringify_single` |
| `type.annotations_en_chaine` | `annotationlib.annotations_to_string` |
| `type.appeler_annoter_interne` | `annotationlib._get_and_call_annotate` |
| `type.appeler_fonction_annoter` | `annotationlib.call_annotate_function` |
| `type.appeler_fonction_evaluer` | `annotationlib.call_evaluate_function` |
| `type.constructeur_modele_ast` | `annotationlib._template_to_ast_constructor` |
| `type.construire_cloture` | `annotationlib._build_closure` |
| `type.literal_modele_ast` | `annotationlib._template_to_ast_literal` |
| `type.modele_vers_ast` | `annotationlib._template_to_ast` |
| `type.obtenir_annotations` | `annotationlib.get_annotations` |
| `type.obtenir_annotations_doubles` | `annotationlib._get_dunder_annotations` |
| `type.obtenir_espace_nom_classe` | `annotationlib.get_annotate_from_class_namespace` |
| `type.reescrire_deballage_etoile` | `annotationlib._rewrite_star_unpack` |
| `type.repr_type` | `annotationlib.type_repr` |
| `type.transformer_en_chaine_unique` | `annotationlib._stringify_single` |
| `type_base` | `type` |
| `type_itérateur` | `NATIVE.itype` |
| `type_profond` | `NATIVE.deeptype` |
| `typeprofond` | `NATIVE.deeptype` |
| `variables` | `vars` |
| `variables_contexte.copier_contexte` | `contextvars.copy_context` |
| `volant_inertie` | `NATIVE.flywheel` |
| `vrai_faux` | `bool` |
| `vue_memoire` | `memoryview` |
| `web.analyser_disposition_contenu` | `aiohttp.parse_content_disposition` |
| `web.definir_moteur_zlib` | `aiohttp.set_zlib_backend` |
| `web.nom_fichier_disposition` | `aiohttp.content_disposition_filename` |
| `web.obtenir_donnees_utiles` | `aiohttp.get_payload` |
| `web.requete` | `aiohttp.request` |
| `zipper` | `zip` |


### Méthodes de chaînes

| Frython | Python |
|---------|--------|
| `aligner_droite` | `rjust` |
| `aligner_gauche` | `ljust` |
| `capitaliser` | `capitalize` |
| `centrer` | `center` |
| `commencer_par` | `startswith` |
| `compter` | `count` |
| `compter_depuis` | `count` |
| `compter_tout` | `count` |
| `contient` | `__contains__` |
| `decoder` | `decode` |
| `diviser` | `split` |
| `diviser_droite` | `rsplit` |
| `diviser_lignes` | `splitlines` |
| `en_liste` | `split` |
| `encoder` | `encode` |
| `est_alpha` | `isalpha` |
| `est_alphanum` | `isalnum` |
| `est_ascii` | `isascii` |
| `est_decimal` | `isdecimal` |
| `est_digit` | `isdigit` |
| `est_espace` | `isspace` |
| `est_identifiant` | `isidentifier` |
| `est_imprimable` | `isprintable` |
| `est_majuscule` | `isupper` |
| `est_minuscule` | `islower` |
| `est_numerique` | `isnumeric` |
| `est_titre` | `istitle` |
| `expandre_tabs` | `expandtabs` |
| `finir_par` | `endswith` |
| `formater` | `format` |
| `formater_map` | `format_map` |
| `indice` | `index` |
| `joindre` | `join` |
| `majuscule` | `upper` |
| `maketrans` | `maketrans` |
| `minuscule` | `lower` |
| `partitionner` | `partition` |
| `remplacer` | `replace` |
| `remplir_zeros` | `zfill` |
| `rfind` | `rfind` |
| `rindex` | `rindex` |
| `rpartitionner` | `rpartition` |
| `supprimer_espaces` | `strip` |
| `supprimer_espaces_droite` | `rstrip` |
| `supprimer_espaces_gauche` | `lstrip` |
| `supprimer_prefixe` | `removeprefix` |
| `supprimer_suffixe` | `removesuffix` |
| `titrer` | `title` |
| `traduire` | `translate` |
| `trouver` | `find` |


### Méthodes de listes

| Frython | Python |
|---------|--------|
| `ajouter` | `append` |
| `annexer` | `append` |
| `compter` | `count` |
| `concatener` | `extend` |
| `copie_profonde` | `copy` |
| `copier` | `copy` |
| `dernier` | `pop` |
| `effacer` | `clear` |
| `etendre` | `extend` |
| `existe` | `__contains__` |
| `extraire` | `pop` |
| `indice` | `index` |
| `inserer` | `insert` |
| `inserer_debut` | `insert` |
| `inverser` | `reverse` |
| `longueur` | `__len__` |
| `multiplier` | `__mul__` |
| `premier` | `pop` |
| `remplir` | `fill` |
| `remplir_avec` | `extend` |
| `retirer` | `remove` |
| `supprimer` | `remove` |
| `trier` | `sort` |
| `vider` | `clear` |


### Méthodes de dictionnaires

| Frython | Python |
|---------|--------|
| `a_cle` | `has_key` |
| `cles` | `keys` |
| `contient` | `__contains__` |
| `contient_cle` | `__contains__` |
| `copier` | `copy` |
| `depuis_cles` | `fromkeys` |
| `effacer` | `clear` |
| `elements` | `items` |
| `extraire` | `pop` |
| `extraire_defaut` | `setdefault` |
| `extraire_dernier` | `popitem` |
| `fusionner` | `update` |
| `inverser` | `items` |
| `longueur` | `__len__` |
| `mettre_a_jour` | `update` |
| `obtenir` | `get` |
| `obtenir_ou_creer` | `setdefault` |
| `valeurs` | `values` |
| `vider` | `clear` |


### Méthodes d'ensembles

| Frython | Python |
|---------|--------|
| `ajouter` | `add` |
| `copier` | `copy` |
| `diff_sym_sur_place` | `symmetric_difference_update` |
| `difference` | `difference` |
| `difference_sur_place` | `difference_update` |
| `difference_symetrique` | `symmetric_difference` |
| `ecarter` | `discard` |
| `est_disjoint` | `isdisjoint` |
| `est_sous_ensemble` | `issubset` |
| `est_sur_ensemble` | `issuperset` |
| `est_vide` | `__len__` |
| `extraire_aleatoire` | `pop` |
| `geler` | `frozenset` |
| `intersection` | `intersection` |
| `intersection_sur_place` | `intersection_update` |
| `mettre_a_jour` | `update` |
| `retirer` | `remove` |
| `supprimer_si_existe` | `discard` |
| `union` | `union` |
| `union_sur_place` | `update` |
| `vider` | `clear` |


### Modules traduits

| Frython | Python |
|---------|--------|
| `abstrait` | `abc` |
| `aleatoire` | `random` |
| `archive` | `tarfile` |
| `argparse` | `argparse` |
| `arguments` | `argparse` |
| `ast_module` | `ast` |
| `async_io` | `asyncio` |
| `base64` | `base64` |
| `base_donnees` | `sqlite3` |
| `binaire_io` | `io` |
| `calcul` | `numpy` |
| `chemin` | `os.path` |
| `chemin_fichier` | `pathlib` |
| `chiffrement` | `cryptography` |
| `code_module` | `code` |
| `collections` | `collections` |
| `collections_abc` | `collections.abc` |
| `compression` | `zipfile` |
| `concurrent` | `concurrent.futures` |
| `configparser` | `configparser` |
| `configuration` | `configparser` |
| `contextlib` | `contextlib` |
| `copie` | `copy` |
| `copie_profonde` | `deepcopy` |
| `couleur` | `colorsys` |
| `cryptographie` | `cryptography` |
| `csv` | `csv` |
| `curses` | `curses` |
| `dataclasse` | `dataclasses` |
| `date` | `datetime` |
| `datetime` | `datetime` |
| `debogueur` | `pdb` |
| `decimal_module` | `decimal` |
| `decimal_precision` | `decimal` |
| `difflib` | `difflib` |
| `dis` | `dis` |
| `doctest` | `doctest` |
| `donnees` | `pandas` |
| `email` | `email` |
| `encodage` | `base64` |
| `entree_sortie` | `io` |
| `enum` | `enum` |
| `environnement` | `dotenv` |
| `expression_reguliere` | `re` |
| `fichier_entree` | `fileinput` |
| `fil` | `threading` |
| `fnmatch` | `fnmatch` |
| `fonctionnel` | `functools` |
| `formateur` | `formatter` |
| `fractions` | `fractions` |
| `ftplib` | `ftplib` |
| `functools` | `functools` |
| `futur` | `__future__` |
| `garbage` | `gc` |
| `gestionnaire_contexte` | `contextlib` |
| `glob` | `glob` |
| `graphiques` | `matplotlib` |
| `grp` | `grp` |
| `gzip` | `gzip` |
| `hachage` | `hashlib` |
| `hashlib` | `hashlib` |
| `heapq` | `heapq` |
| `hmac` | `hmac` |
| `html` | `html` |
| `html_analyse` | `html.parser` |
| `http` | `http` |
| `http_client` | `http.client` |
| `http_serveur` | `http.server` |
| `images` | `PIL` |
| `imaplib` | `imaplib` |
| `importlib` | `importlib` |
| `inspection` | `inspect` |
| `interface` | `tkinter` |
| `io` | `io` |
| `ipaddress` | `ipaddress` |
| `iterateurs` | `itertools` |
| `itertools` | `itertools` |
| `journalisation` | `logging` |
| `json` | `json` |
| `locale` | `locale` |
| `logging` | `logging` |
| `lzma` | `lzma` |
| `mailbox` | `mailbox` |
| `marshal` | `marshal` |
| `math` | `math` |
| `mathematiques` | `math` |
| `mathématiques` | `math` |
| `mimetypes` | `mimetypes` |
| `mmap` | `mmap` |
| `msvcrt` | `msvcrt` |
| `multiprocessing` | `multiprocessing` |
| `multiprocessus` | `multiprocessing` |
| `netrc` | `netrc` |
| `nis` | `nis` |
| `nntplib` | `nntplib` |
| `nombres` | `numbers` |
| `operateur` | `operator` |
| `optparse` | `optparse` |
| `os_chemin` | `os.path` |
| `pathlib` | `pathlib` |
| `pickle` | `pickle` |
| `pickletools` | `pickletools` |
| `pipes` | `pipes` |
| `pkgutil` | `pkgutil` |
| `plateforme` | `platform` |
| `poplib` | `poplib` |
| `pprint` | `pprint` |
| `profil` | `cProfile` |
| `pty` | `pty` |
| `pwd` | `pwd` |
| `py_compile` | `py_compile` |
| `pydoc` | `pydoc` |
| `queue` | `queue` |
| `quopri` | `quopri` |
| `re` | `re` |
| `readline` | `readline` |
| `reprlib` | `reprlib` |
| `reseau` | `urllib` |
| `rlcompleter` | `rlcompleter` |
| `runpy` | `runpy` |
| `sched` | `sched` |
| `secret` | `secrets` |
| `secrets` | `secrets` |
| `select` | `select` |
| `selectors` | `selectors` |
| `shelve` | `shelve` |
| `shlex` | `shlex` |
| `shutil` | `shutil` |
| `signal` | `signal` |
| `smtplib` | `smtplib` |
| `sndhdr` | `sndhdr` |
| `socket` | `socket` |
| `sous_processus` | `subprocess` |
| `spwd` | `spwd` |
| `sqlite` | `sqlite3` |
| `sqlite3` | `sqlite3` |
| `ssl` | `ssl` |
| `stat` | `stat` |
| `statistiques` | `statistics` |
| `statistiques_module` | `statistics` |
| `string_module` | `string` |
| `stringprep` | `stringprep` |
| `struct` | `struct` |
| `subprocess` | `subprocess` |
| `systeme` | `sys` |
| `systeme_exploitation` | `os` |
| `tableau_module` | `array` |
| `telnetlib` | `telnetlib` |
| `tempfichier` | `tempfile` |
| `temps` | `time` |
| `terminal` | `tty` |
| `test_rapide` | `pytest` |
| `tests` | `unittest` |
| `textwrap` | `textwrap` |
| `threading` | `threading` |
| `timeit` | `timeit` |
| `tkinter_module` | `tkinter` |
| `token` | `token` |
| `tokenize` | `tokenize` |
| `tomllib` | `tomllib` |
| `tortue` | `turtle` |
| `trace` | `trace` |
| `traceback` | `traceback` |
| `turtle_module` | `turtle` |
| `turtledemo` | `turtledemo` |
| `types_donnees` | `typing` |
| `types_module` | `types` |
| `unicodedata` | `unicodedata` |
| `unittest` | `unittest` |
| `urllib` | `urllib` |
| `urllib_analyse` | `urllib.parse` |
| `urllib_erreur` | `urllib.error` |
| `urllib_requete` | `urllib.request` |
| `uu` | `uu` |
| `uuid` | `uuid` |
| `venv` | `venv` |
| `warnings` | `warnings` |
| `wave` | `wave` |
| `weakref` | `weakref` |
| `web` | `requests` |
| `webbrowser` | `webbrowser` |
| `winreg` | `winreg` |
| `winsound` | `winsound` |
| `wsgiref` | `wsgiref` |
| `xdrlib` | `xdrlib` |
| `xml` | `xml` |
| `xmlrpc` | `xmlrpc` |
| `zipapp` | `zipapp` |
| `zipimport` | `zipimport` |
| `zlib` | `zlib` |
| `zoneinfo` | `zoneinfo` |

<!-- MOTS_CLES_END -->

## 9. Exceptions et erreurs

### Exceptions Frython

| Frython | Python | Description |
|---------|--------|-------------|
| `ErreurValeur` | `ValueError` | Valeur incorrecte |
| `ErreurType` | `TypeError` | Mauvais type |
| `ErreurNom` | `NameError` | Nom non défini |
| `ErreurIndex` | `IndexError` | Indice hors limites |
| `ErreurCle` | `KeyError` | Clé inexistante |
| `ErreurAttribut` | `AttributeError` | Attribut inexistant |
| `ErreurImport` | `ImportError` | Import impossible |
| `ErreurMemoire` | `MemoryError` | Mémoire insuffisante |
| `ErreurRecursion` | `RecursionError` | Récursion infinie |
| `ErreurSyntaxe` | `SyntaxError` | Erreur de syntaxe |
| `ErreurDivisionZero` | `ZeroDivisionError` | Division par zéro |
| `ErreurFichier` | `FileNotFoundError` | Fichier introuvable |
| `ErreurPermission` | `PermissionError` | Permission refusée |
| `ErreurArret` | `StopIteration` | Arrêt d'itération |
| `ErreurOS` | `OSError` | Erreur système |
| `ErreurConnexion` | `ConnectionError` | Erreur de connexion |
| `ErreurDebordement` | `OverflowError` | Dépassement |
| `ErreurRuntime` | `RuntimeError` | Erreur d'exécution |
| `ErreurTimeout` | `TimeoutError` | Délai dépassé |
| `ErreurInterruption` | `KeyboardInterrupt` | Interruption clavier |
| `ErreurAssertion` | `AssertionError` | Assertion échouée |

### Avertissements

| Frython | Python |
|---------|--------|
| `Avertissement` | `Warning` |
| `AvertissementDepreciation` | `DeprecationWarning` |
| `AvertissementRuntime` | `RuntimeWarning` |
| `AvertissementSyntaxe` | `SyntaxWarning` |
| `AvertissementUtilisateur` | `UserWarning` |
| `AvertissementFutur` | `FutureWarning` |

### Exemple de gestion complète

```python
déf lire_fichier(chemin):
    essayer:
        avec ouvrir(chemin, "r") comme f:
            retourner f.lire()
    sauf ErreurFichier:
        afficher(f"Fichier '{chemin}' introuvable!")
        retourner Rien
    sauf ErreurPermission:
        afficher(f"Permission refusée pour '{chemin}'!")
        retourner Rien
    sauf Exception comme e:
        lever ErreurRuntime(f"Erreur inattendue: {e}")
    enfin:
        afficher("Tentative de lecture terminée.")
```

---

## 10. Exemples complets

### Calculatrice

```python
# calculatrice.fy
tantque Vrai:
    essayer:
        entree = saisir(">>> ")
        si entree dans ("quitter", "q"):
            casser
        afficher(f"= {eval(entree)}")
    sauf ZeroDivisionError:
        afficher("Division par zéro!")
    sauf Exception:
        afficher("Expression invalide.")
```

### Fibonacci

```python
# fibonacci.fy
déf fibonacci(n):
    si n <= 1:
        retourner n
    retourner fibonacci(n-1) + fibonacci(n-2)

pour i dans intervalle(15):
    afficher(f"F({i}) = {fibonacci(i)}")
```

### Tri à bulles

```python
# tri_bulles.fy
déf tri_bulles(lst):
    arr = liste(lst)
    n = longueur(arr)
    pour i dans intervalle(n):
        pour j dans intervalle(0, n - i - 1):
            si arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    retourner arr

nombres = [64, 34, 25, 12, 22, 11, 90]
afficher(tri_bulles(nombres))
```

---

## 11. API Python

Vous pouvez utiliser Frython comme bibliothèque Python :

```python
from frython import transpiler, InterpreteurFrython

# Transpiler uniquement
code_python = transpiler("""
déf bonjour(nom):
    afficher(f"Bonjour, {nom}!")
bonjour("Monde")
""")
print(code_python)

# Exécuter
interp = InterpreteurFrython()
interp.executer_source(code_frython)

# Exécuter un fichier
interp.executer_fichier("mon_programme.fy")
```

---

## 12. Architecture interne

### Fichiers principaux

```
frython/
├── __init__.py      # Point d'entrée, exports publics
├── lexeur.py        # Tokenizer (analyse lexicale)
├── transpileur.py   # Cœur : traduit Frython → Python
└── interpreteur.py  # REPL et exécution
```

### Le transpileur

Le transpileur fonctionne en plusieurs étapes :

1. **Séparation des chaînes** — protège le contenu des strings
2. **Traduction des méthodes** — `.ajouter()` → `.append()`
3. **Traduction des modules** — `mathématiques` → `math`
4. **Traduction des mots-clés** — `si` → `if`, `afficher` → `print`
5. **Traduction des f-strings** — traduit les expressions à l'intérieur des `{}`

### Dictionnaires de traduction

- `MOTS_CLES_VERS_PYTHON` — mots-clés et fonctions globales
- `METHODES_CHAINE` — méthodes de chaînes
- `METHODES_LISTE` — méthodes de listes
- `METHODES_DICT` — méthodes de dictionnaires
- `METHODES_ENSEMBLE` — méthodes d'ensembles
- `MODULES_TRADUITS` — noms de modules

---

## 13. Extension VS Code

Une extension VS Code est disponible pour Frython avec :

- **Coloration syntaxique** complète pour les fichiers `.fy`
- **Snippets** pour écrire du Frython rapidement
- **Auto-indentation** après `:`
- **Auto-fermeture** des paires de caractères

### Snippets disponibles

| Préfixe | Description |
|---------|-------------|
| `aff` | `afficher()` |
| `afff` | `afficher()` avec f-string |
| `si` | Bloc si/sinon |
| `sisi` | Bloc si/sinonsi/sinon |
| `def` | Définir une fonction |
| `defr` | Fonction avec retour |
| `cls` | Définir une classe |
| `clsh` | Classe avec héritage |
| `tq` | Boucle tantque |
| `pour` | Boucle pour/dans |
| `pouri` | Boucle pour avec intervalle |
| `poure` | Boucle pour avec enumerer |
| `ess` | Bloc essayer/sauf |
| `esse` | Bloc essayer/sauf/enfin |
| `imp` | Importer |
| `impd` | Importer depuis |
| `lev` | Lever une erreur |
| `comp` | Compréhension de liste |
| `compc` | Compréhension avec condition |
| `lam` | Lambda |
| `avec` | Gestionnaire de contexte |
| `main` | Garde principale |
| `doc` | Docstring complète |

---

## 14. FAQ

**Q: Frython est-il vraiment utilisable en production ?**  
R: Techniquement oui — le code transpilé est du Python valide. En pratique, votre équipe va vous regarder bizarrement.

**Q: Puis-je utiliser des bibliothèques Python externes ?**  
R: Oui, toutes. `importer numpy comme np` fonctionne parfaitement.

**Q: Les f-strings fonctionnent-elles ?**  
R: Oui, et les expressions à l'intérieur des `{}` sont aussi traduites.

**Q: Puis-je mixer Frython et Python dans le même fichier ?**  
R: Oui — `def` et `déf` sont tous les deux supportés, `True` et `Vrai` aussi.

**Q: Frython supporte-t-il async/await ?**  
R: Oui — `asynchrone` et `attendre`.

**Q: Les accents dans les noms de variables sont-ils supportés ?**  
R: Pour les mots-clés et méthodes oui. Pour les noms de variables, ça dépend de votre version de Python.

**Q: Pourquoi ce projet existe-t-il ?**  
R: *Pourquoi pas ?* 🥐

---

## 15. Contribuer

### Comment contribuer

1. Forkez le repo : `https://github.com/Artleboss2/frython`
2. Créez une branche : `git checkout -b feature/ma-feature`
3. Faites vos changements
4. Lancez les tests : `python -m unittest tests/test_frython.py -v`
5. Committez : `git commit -m "feat: ma feature"`
6. Push : `git push origin feature/ma-feature`
7. Ouvrez une Pull Request

### Idées de contributions

- Ajouter de nouveaux mots-clés français
- Améliorer les messages d'erreur en français
- Créer des exemples de programmes
- Ajouter des tests
- Améliorer la documentation
- Créer des tutoriels
- Traduire dans d'autres langues (*Pythonisch ? Pythönen ?*)

### Standards de code

- Tests requis pour toute nouvelle fonctionnalité
- Docstrings en français
- Messages de commit en anglais ou français

---

*Documentation générée pour Frython v1.0.2 — 🐓 Python en français, sacré bleu !*
