# 📝 Historique des mises à jour — Frython

> Tous les changements notables du projet Frython, dans l'ordre chronologique.

---

## [1.0.9] — 2026-03-22


### Ajouté

- **Mots-clés et fonctions** — 172 nouveau(x):
  - `abc._enregistrer` → `abc._abc_register`
  - `abc._initialisation_interne` → `abc._abc_init`
  - `abc._obtenir_decharge` → `abc._get_dump`
  - `abc._reinitialiser_caches` → `abc._reset_caches`
  - `abc._reinitialiser_registre` → `abc._reset_registry`
  - `abc._verifier_instance` → `abc._abc_instancecheck`
  - `abc._verifier_sous_classe` → `abc._abc_subclasscheck`
  - `abc.actualiser_methodes_abstraites` → `abc.update_abstractmethods`
  - `abc.enregistrer` → `abc._abc_register`
  - `abc.initialisation_interne` → `abc._abc_init`
  - `abc.methode_abstraite` → `abc.abstractmethod`
  - `abc.obtenir_decharge` → `abc._get_dump`
  - `abc.obtenir_jeton_cache` → `abc.get_cache_token`
  - `abc.reinitialiser_caches` → `abc._reset_caches`
  - `abc.reinitialiser_registre` → `abc._reset_registry`
  - `abc.verifier_instance` → `abc._abc_instancecheck`
  - `abc.verifier_sous_classe` → `abc._abc_subclasscheck`
  - `antigravite.hachage_geo` → `antigravity.geohash`
  - `anyio.attendre_lisible` → `anyio.wait_readable`
  - `anyio.attendre_scriptible` → `anyio.wait_writable`
  - `anyio.connecter_tcp` → `anyio.connect_tcp`
  - `anyio.connecter_unix` → `anyio.connect_unix`
  - `anyio.continuer_apres` → `anyio.move_on_after`
  - `anyio.creer_ecouteur_tcp` → `anyio.create_tcp_listener`
  - `anyio.creer_ecouteur_unix` → `anyio.create_unix_listener`
  - `anyio.creer_fichier_temp` → `anyio.mkstemp`
  - `anyio.creer_groupe_taches` → `anyio.create_task_group`
  - `anyio.creer_repertoire_temp` → `anyio.mkdtemp`
  - `anyio.creer_socket_udp` → `anyio.create_udp_socket`
  - `anyio.creer_socket_udp_connecte` → `anyio.create_connected_udp_socket`
  - `anyio.deadline_actuelle` → `anyio.current_effective_deadline`
  - `anyio.dormir` → `anyio.sleep`
  - `anyio.dormir_jusqua` → `anyio.sleep_until`
  - `anyio.dormir_toujours` → `anyio.sleep_forever`
  - `anyio.echouer_apres` → `anyio.fail_after`
  - `anyio.envelopper_fichier` → `anyio.wrap_file`
  - `anyio.fermer_de_force` → `anyio.aclose_forcefully`
  - `anyio.lancer` → `anyio.run`
  - `anyio.lancer_processus` → `anyio.run_process`
  - `anyio.notifier_fermeture` → `anyio.notify_closing`
  - `anyio.obtenir_moteurs_disponibles` → `anyio.get_available_backends`
  - `anyio.obtenir_repertoire_temp` → `anyio.gettempdir`
  - `anyio.obtenir_tache_actuelle` → `anyio.get_current_task`
  - `anyio.obtenir_taches_en_cours` → `anyio.get_running_tasks`
  - `anyio.obtenir_tous_les_moteurs` → `anyio.get_all_backends`
  - `anyio.ouvrir_fichier` → `anyio.open_file`
  - `anyio.ouvrir_processus` → `anyio.open_process`
  - `anyio.temps_actuel` → `anyio.current_time`
  - `arguments._copier_elements` → `argparse._copy_items`
  - `arguments._nom_programme` → `argparse._prog_name`
  - `arguments._obtenir_nom_action` → `argparse._get_action_name`
  - `arguments.copier_elements` → `argparse._copy_items`
  - `arguments.n_obtenir_texte` → `argparse.ngettext`
  - `arguments.nom_programme` → `argparse._prog_name`
  - `arguments.obtenir_nom_action` → `argparse._get_action_name`
  - `ast._definir_dims` → `ast._dims_setter`
  - `ast._diviser_lignes_sans_ff` → `ast._splitlines_no_ff`
  - `ast._obtenir_dims` → `ast._dims_getter`
  - `ast._remplir_espaces` → `ast._pad_whitespace`
  - `ast.analyser` → `ast.parse`
  - `ast.comparer` → `ast.compare`
  - `ast.copier_emplacement` → `ast.copy_location`
  - `ast.corriger_emplacements` → `ast.fix_missing_locations`
  - `ast.decharger` → `ast.dump`
  - `ast.definir_dims` → `ast._dims_setter`
  - `ast.desanalyser` → `ast.unparse`
  - `ast.diviser_lignes_sans_ff` → `ast._splitlines_no_ff`
  - `ast.evaluer_litteral` → `ast.literal_eval`
  - `ast.incrementer_ligne` → `ast.increment_lineno`
  - `ast.iterer_champs` → `ast.iter_fields`
  - `ast.iterer_noeuds_enfants` → `ast.iter_child_nodes`
  - `ast.obtenir_dims` → `ast._dims_getter`
  - `ast.obtenir_docstring` → `ast.get_docstring`
  - `ast.obtenir_segment_source` → `ast.get_source_segment`
  - `ast.parcourir` → `ast.walk`
  - `ast.remplir_espaces` → `ast._pad_whitespace`
  - `asyncio._desenregistrer_tache` → `asyncio._unregister_task`
  - `asyncio._enregistrer_tache` → `asyncio._register_task`
  - `asyncio._entrer_dans_tache` → `asyncio._enter_task`
  - `asyncio._quitter_tache` → `asyncio._leave_task`
  - `asyncio.assurer_futur` → `asyncio.ensure_future`
  - `asyncio.attendre` → `asyncio.wait`
  - `asyncio.attendre_pendant` → `asyncio.wait_for`
  - `asyncio.au_fur_et_a_mesure` → `asyncio.as_completed`
  - `asyncio.bouclier` → `asyncio.shield`
  - `asyncio.creer_sous_processus_exec` → `asyncio.create_subprocess_exec`
  - `asyncio.creer_sous_processus_shell` → `asyncio.create_subprocess_shell`
  - `asyncio.creer_tache` → `asyncio.create_task`
  - `asyncio.definir_boucle` → `asyncio.set_event_loop`
  - `asyncio.delai_limite` → `asyncio.timeout`
  - `asyncio.delai_limite_a` → `asyncio.timeout_at`
  - `asyncio.demarrer_serveur` → `asyncio.start_server`
  - `asyncio.desenregistrer_tache` → `asyncio._unregister_task`
  - `asyncio.dormir` → `asyncio.sleep`
  - `asyncio.enregistrer_tache` → `asyncio._register_task`
  - `asyncio.entrer_dans_tache` → `asyncio._enter_task`
  - `asyncio.envelopper_futur` → `asyncio.wrap_future`
  - `asyncio.est_coroutine` → `asyncio.iscoroutine`
  - `asyncio.est_fonction_coroutine` → `asyncio.iscoroutinefunction`
  - `asyncio.est_futur` → `asyncio.isfuture`
  - `asyncio.lancer` → `asyncio.run`
  - `asyncio.lancer_coroutine_filetée` → `asyncio.run_coroutine_threadsafe`
  - `asyncio.nouvelle_boucle` → `asyncio.new_event_loop`
  - `asyncio.obtenir_boucle` → `asyncio.get_event_loop`
  - `asyncio.obtenir_boucle_actuelle` → `asyncio.get_running_loop`
  - `asyncio.ouvrir_connexion` → `asyncio.open_connection`
  - `asyncio.quitter_tache` → `asyncio._leave_task`
  - `asyncio.rassembler` → `asyncio.gather`
  - `asyncio.tache_actuelle` → `asyncio.current_task`
  - `asyncio.toutes_les_taches` → `asyncio.all_tasks`
  - `asyncio.vers_fil` → `asyncio.to_thread`
  - `attr.a` → `attr.has`
  - `attr.associer` → `attr.assoc`
  - `attr.attribut` → `attr.attrib`
  - `attr.champ` → `attr.field`
  - `attr.champs` → `attr.fields`
  - `attr.comparer_avec` → `attr.cmp_using`
  - `attr.creer_classe` → `attr.make_class`
  - `attr.definir` → `attr.define`
  - `attr.dict_champs` → `attr.fields_dict`
  - `attr.en_dict` → `attr.asdict`
  - `attr.en_tuple` → `attr.astuple`
  - `attr.evoluer` → `attr.evolve`
  - `attr.mutable` → `attr.mutable`
  - `attr.resoudre_types` → `attr.resolve_types`
  - `attr.valider` → `attr.validate`
  - `attrs.a` → `attrs.has`
  - `attrs.associer` → `attrs.assoc`
  - `attrs.champs` → `attrs.fields`
  - `attrs.comparer_avec` → `attrs.cmp_using`
  - `attrs.creer_classe` → `attrs.make_class`
  - `attrs.definir` → `attrs.define`
  - `attrs.dict_champs` → `attrs.fields_dict`
  - `attrs.en_dict` → `attrs.asdict`
  - `attrs.en_tuple` → `attrs.astuple`
  - `attrs.evoluer` → `attrs.evolve`
  - `attrs.field` → `attrs.field`
  - `attrs.inspecter` → `attrs.inspect`
  - `attrs.mutable` → `attrs.mutable`
  - `attrs.resoudre_types` → `attrs.resolve_types`
  - `attrs.valider` → `attrs.validate`
  - `reseau.adresse_vers_infos` → `aiohappyeyeballs.addr_to_addr_infos`
  - `reseau.demarrer_connexion` → `aiohappyeyeballs.start_connection`
  - `reseau.extraire_infos_entrelacees` → `aiohappyeyeballs.pop_addr_infos_interleave`
  - `reseau.supprimer_infos_adresse` → `aiohappyeyeballs.remove_addr_infos`
  - `type._appeler_annoter_interne` → `annotationlib._get_and_call_annotate`
  - `type._constructeur_modele_ast` → `annotationlib._template_to_ast_constructor`
  - `type._construire_cloture` → `annotationlib._build_closure`
  - `type._literal_modele_ast` → `annotationlib._template_to_ast_literal`
  - `type._modele_vers_ast` → `annotationlib._template_to_ast`
  - `type._obtenir_annotations_doubles` → `annotationlib._get_dunder_annotations`
  - `type._reescrire_deballage_etoile` → `annotationlib._rewrite_star_unpack`
  - `type._transformer_en_chaine_unique` → `annotationlib._stringify_single`
  - `type.annotations_en_chaine` → `annotationlib.annotations_to_string`
  - `type.appeler_annoter_interne` → `annotationlib._get_and_call_annotate`
  - `type.appeler_fonction_annoter` → `annotationlib.call_annotate_function`
  - `type.appeler_fonction_evaluer` → `annotationlib.call_evaluate_function`
  - `type.constructeur_modele_ast` → `annotationlib._template_to_ast_constructor`
  - `type.construire_cloture` → `annotationlib._build_closure`
  - `type.literal_modele_ast` → `annotationlib._template_to_ast_literal`
  - `type.modele_vers_ast` → `annotationlib._template_to_ast`
  - `type.obtenir_annotations` → `annotationlib.get_annotations`
  - `type.obtenir_annotations_doubles` → `annotationlib._get_dunder_annotations`
  - `type.obtenir_espace_nom_classe` → `annotationlib.get_annotate_from_class_namespace`
  - `type.reescrire_deballage_etoile` → `annotationlib._rewrite_star_unpack`
  - `type.repr_type` → `annotationlib.type_repr`
  - `type.transformer_en_chaine_unique` → `annotationlib._stringify_single`
  - `web.analyser_disposition_contenu` → `aiohttp.parse_content_disposition`
  - `web.definir_moteur_zlib` → `aiohttp.set_zlib_backend`
  - `web.nom_fichier_disposition` → `aiohttp.content_disposition_filename`
  - `web.obtenir_donnees_utiles` → `aiohttp.get_payload`
  - `web.requete` → `aiohttp.request`

---


## [1.0.8] — 2026-03-22


### Ajouté

- **Mots-clés et fonctions** — 63 nouveau(x):
  - `__construire_classe__` → `NATIVE.__build_class__`
  - `__importer__` → `NATIVE.__import__`
  - `abs` → `NATIVE.abs`
  - `accumulateur` → `NATIVE.flywheel`
  - `afficher_pile` → `NATIVE.printStack`
  - `afficher_pile_inverse` → `NATIVE.printReverseStack`
  - `afficher_pile_verbeuse` → `NATIVE.printVerboseStack`
  - `ajouterStr` → `NATIVE.appendStr`
  - `anext` → `NATIVE.anext`
  - `appelable` → `NATIVE.callable`
  - `appendStr` → `NATIVE.appendStr`
  - `asuivant` → `NATIVE.anext`
  - `bin` → `NATIVE.bin`
  - `bound` → `NATIVE.bound`
  - `callable` → `NATIVE.callable`
  - `certains` → `NATIVE.any`
  - `chr` → `NATIVE.chr`
  - `clamp` → `NATIVE.clamp`
  - `collecte_pstat` → `NATIVE.pstatcollect`
  - `compile` → `NATIVE.compile`
  - `configIsToday` → `NATIVE.configIsToday`
  - `configurationEstAujourdhui` → `NATIVE.configIsToday`
  - `creer_liste` → `NATIVE.makeList`
  - `creer_tuple` → `NATIVE.makeTuple`
  - `dictionnaire_histogramme` → `NATIVE.histogramDict`
  - `div_reste` → `NATIVE.divmod`
  - `divreste` → `NATIVE.divmod`
  - `erreur_enregistree` → `NATIVE.exceptionLogged`
  - `exception_enregistree` → `NATIVE.exceptionLogged`
  - `exception_journalisee` → `NATIVE.exceptionLogged`
  - `formater` → `NATIVE.format`
  - `generateur_boucle` → `NATIVE.loopGen`
  - `generateur_nul` → `NATIVE.nullGen`
  - `interpolation_linéaire` → `NATIVE.lerp`
  - `inverser_dictionnaire` → `NATIVE.invertDict`
  - `inverser_dictionnaire_sans_perte` → `NATIVE.invertDictLossless`
  - `journaliser_bloc` → `NATIVE.logBlock`
  - `lerp` → `NATIVE.lerp`
  - `lien` → `NATIVE.bound`
  - `limite` → `NATIVE.bound`
  - `n_importe_quel` → `NATIVE.any`
  - `nom_type` → `NATIVE.typeName`
  - `nom_type_securise` → `NATIVE.safeTypeName`
  - `nom_unique` → `NATIVE.uniqueName`
  - `numero_serie` → `NATIVE.serialNum`
  - `obtenir_base` → `NATIVE.getBase`
  - `obtenir_depot` → `NATIVE.getRepository`
  - `pince` → `NATIVE.clamp`
  - `point_de_rupture` → `NATIVE.breakpoint`
  - `pointderupture` → `NATIVE.breakpoint`
  - `profile` → `NATIVE.profiled`
  - `rapport` → `NATIVE.report`
  - `regulateur` → `NATIVE.flywheel`
  - `rep` → `NATIVE.dir`
  - `repr_rapide` → `NATIVE.fastRepr`
  - `repr_securise` → `NATIVE.safeRepr`
  - `representation_rapide` → `NATIVE.fastRepr`
  - `serrer` → `NATIVE.clamp`
  - `suivant_async` → `NATIVE.anext`
  - `type_itérateur` → `NATIVE.itype`
  - `type_profond` → `NATIVE.deeptype`
  - `typeprofond` → `NATIVE.deeptype`
  - `volant_inertie` → `NATIVE.flywheel`

---


## [1.0.7] — 2026-03-22


### Ajouté

- **Mots-clés et fonctions** — 13 nouveau(x):
  - `a_attribut` → `hasattr`
  - `aiter` → `aiter`
  - `ascii` → `ascii`
  - `compiler` → `compile`
  - `definir_attribut` → `setattr`
  - `importer_module` → `__import__`
  - `index` → `__index__`
  - `obtenir_attribut` → `getattr`
  - `prochain_async` → `anext`
  - `repertoire` → `dir`
  - `supprimer_attribut` → `delattr`
  - `variables` → `vars`
  - `vue_memoire` → `memoryview`
- **Modules traduits** — 105 nouveau(x):
  - `ast_module` → `ast`
  - `code_module` → `code`
  - `collections_abc` → `collections.abc`
  - `concurrent` → `concurrent.futures`
  - `cryptographie` → `cryptography`
  - `curses` → `curses`
  - `debogueur` → `pdb`
  - `difflib` → `difflib`
  - `dis` → `dis`
  - `doctest` → `doctest`
  - `fichier_entree` → `fileinput`
  - `fnmatch` → `fnmatch`
  - `formateur` → `formatter`
  - `ftplib` → `ftplib`
  - `futur` → `__future__`
  - `gestionnaire_contexte` → `contextlib`
  - `glob` → `glob`
  - `grp` → `grp`
  - `gzip` → `gzip`
  - `heapq` → `heapq`
  - `hmac` → `hmac`
  - `html_analyse` → `html.parser`
  - `http_client` → `http.client`
  - `http_serveur` → `http.server`
  - `imaplib` → `imaplib`
  - `importlib` → `importlib`
  - `ipaddress` → `ipaddress`
  - `locale` → `locale`
  - `lzma` → `lzma`
  - `mailbox` → `mailbox`
  - `marshal` → `marshal`
  - `math` → `math`
  - `mimetypes` → `mimetypes`
  - `mmap` → `mmap`
  - `msvcrt` → `msvcrt`
  - `netrc` → `netrc`
  - `nis` → `nis`
  - `nntplib` → `nntplib`
  - `operateur` → `operator`
  - `optparse` → `optparse`
  - `os_chemin` → `os.path`
  - `pickle` → `pickle`
  - `pickletools` → `pickletools`
  - `pipes` → `pipes`
  - `pkgutil` → `pkgutil`
  - `poplib` → `poplib`
  - `pprint` → `pprint`
  - `profil` → `cProfile`
  - `pty` → `pty`
  - `pwd` → `pwd`
  - `py_compile` → `py_compile`
  - `pydoc` → `pydoc`
  - `queue` → `queue`
  - `quopri` → `quopri`
  - `readline` → `readline`
  - `reprlib` → `reprlib`
  - `rlcompleter` → `rlcompleter`
  - `runpy` → `runpy`
  - `sched` → `sched`
  - `secrets` → `secrets`
  - `select` → `select`
  - `selectors` → `selectors`
  - `shelve` → `shelve`
  - `shlex` → `shlex`
  - `shutil` → `shutil`
  - `smtplib` → `smtplib`
  - `sndhdr` → `sndhdr`
  - `spwd` → `spwd`
  - `sqlite` → `sqlite3`
  - `ssl` → `ssl`
  - `stat` → `stat`
  - `statistiques_module` → `statistics`
  - `string_module` → `string`
  - `stringprep` → `stringprep`
  - `tableau_module` → `array`
  - `telnetlib` → `telnetlib`
  - `tempfichier` → `tempfile`
  - `terminal` → `tty`
  - `textwrap` → `textwrap`
  - `timeit` → `timeit`
  - `tkinter_module` → `tkinter`
  - `token` → `token`
  - `tokenize` → `tokenize`
  - `tomllib` → `tomllib`
  - `trace` → `trace`
  - `turtle_module` → `turtle`
  - `turtledemo` → `turtledemo`
  - `types_module` → `types`
  - `unicodedata` → `unicodedata`
  - `urllib_analyse` → `urllib.parse`
  - `urllib_erreur` → `urllib.error`
  - `urllib_requete` → `urllib.request`
  - `uu` → `uu`
  - `venv` → `venv`
  - `wave` → `wave`
  - `webbrowser` → `webbrowser`
  - `winreg` → `winreg`
  - `winsound` → `winsound`
  - `wsgiref` → `wsgiref`
  - `xdrlib` → `xdrlib`
  - `xmlrpc` → `xmlrpc`
  - `zipapp` → `zipapp`
  - `zipimport` → `zipimport`
  - `zlib` → `zlib`
  - `zoneinfo` → `zoneinfo`

---


## [1.0.6] — 2026-03-22


### Ajouté

- **Mots-clés et fonctions** — 2 nouveau(x):
  - `afficher_format` → `format`
  - `memoire` → `memoryview`
- **Méthodes de chaînes** — 1 nouveau(x):
  - `en_liste` → `split`
- **Méthodes de dictionnaires** — 1 nouveau(x):
  - `a_cle` → `has_key`
- **Modules traduits** — 1 nouveau(x):
  - `decimal_precision` → `decimal`

---


## [1.0.5] — 2026-03-22


### Ajouté

- **Mots-clés et fonctions** — 1 nouveau(x):
  - `entree_erreur` → `stderr`
- **Méthodes de listes** — 1 nouveau(x):
  - `remplir_avec` → `extend`
- **Modules traduits** — 1 nouveau(x):
  - `couleur` → `colorsys`

---


## [1.0.4] — 2026-03-22


### Ajouté

- **Mots-clés et fonctions** — 1 nouveau(x):
  - `imprimer_erreur` → `sys.stderr.write`
- **Méthodes de listes** — 1 nouveau(x):
  - `remplir` → `fill`
- **Modules traduits** — 1 nouveau(x):
  - `tortue` → `turtle`

---


## [1.0.3] — 2026-03-22


### Supprimé

- **Méthodes de dictionnaires** — 1 supprimé(s):
  - `supprimer` (était `__delitem__`)

---


## [1.0.2] — 2026-03-20

### Ajouté
- Fichier `DOCUMENTATION.md` — documentation complète du langage
- Fichier `UPDATE.md` — historique des changements
- Fichier `.gitattributes` — détection du langage Frython par GitHub
- Fichier `languages.yml` — définition officielle du langage pour GitHub Linguist
- Extension VS Code — coloration syntaxique pour les fichiers `.fy`
- Snippets VS Code — raccourcis pour écrire du Frython rapidement
- Fichier `CODE-OF-CONDUCT.md` — code de conduite de la communauté
- Fichier `CONTRIBUTING.md` — guide de contribution

### Amélioré
- Coloration syntaxique VS Code — ajout des appels de fonctions, méthodes, opérateurs, f-strings
- `interpreteur.py` — correction du module `readline` sur Windows (ImportError silencieux)
- `transpileur.py` — correction de la priorité des méthodes (`.ajouter()` → `.append()` au lieu de `.add()`)
- `transpileur.py` — traduction des expressions dans les f-strings (`{soi.nom}` → `{self.nom}`)
- `transpileur.py` — ajout de dizaines de mots-clés, méthodes et modules traduits

---

## [1.0.1] — 2026-03-19

### Ajouté
- Publication sur **PyPI** — `pip install frython` fonctionne mondialement
- Workflow GitHub Actions `.github/workflows/publish.yml` — publication automatique sur PyPI
- Exemples supplémentaires :
  - `calculatrice.fy` — calculatrice interactive
  - `devine_nombre.fy` — jeu de devinettes
  - `todo.fy` — gestionnaire de tâches
  - `carnet_contacts.fy` — carnet d'adresses
  - `pendu.fy` — jeu du pendu
  - `rpg.fy` — mini RPG complet
  - `algorithmes_tri.fy` — 5 algorithmes de tri avec benchmarks
  - `statistiques.fy` — statistiques et histogramme ASCII
  - `analyse_texte.fy` — analyseur de texte
  - `art_ascii.fy` — Mandelbrot, Pascal, spirale
  - `avance.fy` — décorateurs, générateurs, closures

### Corrigé
- `pyproject.toml` — correction du backend setuptools pour Python 3.14
- Compatibilité Windows — suppression de la dépendance `readline`

---

## [1.0.0] — 2026-03-19

### Ajouté — Version initiale

#### Cœur du langage
- `frython/transpileur.py` — transpileur Frython → Python
  - Dictionnaire `MOTS_CLES_VERS_PYTHON` — tous les mots-clés Python traduits en français
  - Dictionnaire `METHODES_CHAINE` — méthodes de chaînes traduites
  - Dictionnaire `METHODES_LISTE` — méthodes de listes traduites
  - Dictionnaire `METHODES_DICT` — méthodes de dictionnaires traduites
  - Dictionnaire `METHODES_ENSEMBLE` — méthodes d'ensembles traduites
  - Dictionnaire `MODULES_TRADUITS` — noms de modules traduits
  - Protection des chaînes de caractères (les strings ne sont pas modifiées)
  - Traduction des expressions dans les f-strings

- `frython/interpreteur.py` — interpréteur et REPL
  - REPL interactive avec prompt `🐓 >>>`
  - Exécution de fichiers `.fy`
  - Messages d'erreur traduits en français
  - Commandes spéciales : `quitter()`, `mots_cles()`
  - Bannière ASCII art au démarrage

- `frython/lexeur.py` — lexeur/tokenizer
  - Support des caractères accentués français
  - Gestion de l'indentation (INDENT/DEDENT)
  - Tous les types de tokens Python

- `frython/__init__.py` — point d'entrée du paquet
- `__main__.py` — interface en ligne de commande complète

#### Mots-clés supportés (version initiale)
- Contrôle de flux : `si`, `sinon`, `sinonsi`, `tantque`, `pour`, `dans`, `casser`, `continuer`, `passer`
- Définitions : `déf`, `retourner`, `classe`, `soi`, `lambda`, `rendement`, `asynchrone`, `attendre`
- Valeurs : `Vrai`, `Faux`, `Rien`
- Logique : `et`, `ou`, `non`, `est`, `pasdans`
- Import : `importer`, `de`, `comme`
- Exceptions : `essayer`, `sauf`, `enfin`, `lever`, `avec`, `affirmer`
- Fonctions : `afficher`, `saisir`, `longueur`, `intervalle`, `liste`, `dictionnaire`, `ensemble`, `tuple`, `entier`, `decimal`, `chaine`, `booleen`, `enumerer`, `zipper`, `mapper`, `filtrer`, `trier`, `inverser`, `somme`, `maximum`, `minimum`, `absolu`, `arrondir`, `aide`, `type`, `super`

#### Tests
- `tests/test_frython.py` — 48 tests unitaires
  - `TestsTranspileur` — 20 tests de transpilation
  - `TestsExecution` — 26 tests d'exécution complète
  - `TestsInterpreteur` — 2 tests de l'interpréteur

#### Exemples initiaux
- `exemples/bonjour_monde.fy` — Hello World
- `exemples/fibonacci.fy` — Suite de Fibonacci
- `exemples/classes.fy` — Programmation orientée objet
- `exemples/vitrine.fy` — Démonstration complète de toutes les fonctionnalités

#### Documentation et configuration
- `README.md` — documentation principale avec badges
- `LICENSE` — licence MIT
- `.gitignore` — fichiers ignorés par Git
- `setup.py` — configuration du paquet Python
- `pyproject.toml` — configuration moderne du build

---

## Roadmap — À venir

### [1.1.0] — Prévu

- [ ] Meilleurs messages d'erreur en français
- [ ] Support complet de `async`/`await`
- [ ] Plugin JetBrains (PyCharm)
- [ ] Documentation interactive en ligne
- [ ] Mode strict (refuse le Python non-traduit)
- [ ] `frython lint` — vérificateur de style

### [2.0.0] — Vision long terme

- [ ] Vrai parser AST (au lieu du transpileur regex)
- [ ] Débogueur intégré
- [ ] Support de la traduction vers d'autres langues
- [ ] Frython dans le navigateur (WebAssembly)
- [ ] Reconnaissance officielle par GitHub Linguist

---

## Format des versions

Ce projet suit [Semantic Versioning](https://semver.org/) :
- **MAJEUR** — changements incompatibles avec l'ancienne syntaxe
- **MINEUR** — nouvelles fonctionnalités rétrocompatibles
- **PATCH** — corrections de bugs

---

*🐓 Frython — Python en français, sacré bleu !*  
*github.com/Artleboss2/frython*
