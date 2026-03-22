# 📝 Historique des mises à jour — Frython

> Tous les changements notables du projet Frython, dans l'ordre chronologique.

---

## [1.0.10] — 2026-03-22


### Ajouté

- **Mots-clés et fonctions** — 311 nouveau(x):
  - `base64._octets_depuis_donnees_decodees` → `base64._bytes_from_decode_data`
  - `base64._verification_type_entree` → `base64._input_type_check`
  - `base64.a85_decoder` → `base64.a85decode`
  - `base64.a85_encoder` → `base64.a85encode`
  - `base64.b16_decoder` → `base64.b16decode`
  - `base64.b16_encoder` → `base64.b16encode`
  - `base64.b32_decoder` → `base64.b32decode`
  - `base64.b32_encoder` → `base64.b32encode`
  - `base64.b64_decoder` → `base64.b64decode`
  - `base64.b64_encoder` → `base64.b64encode`
  - `base64.b64_url_decoder` → `base64.urlsafe_b64decode`
  - `base64.b64_url_encoder` → `base64.urlsafe_b64encode`
  - `base64.decoder` → `base64.decode`
  - `base64.decoder_octets` → `base64.decodebytes`
  - `base64.encoder` → `base64.encode`
  - `base64.encoder_octets` → `base64.encodebytes`
  - `base64.octets_depuis_donnees_decodees` → `base64._bytes_from_decode_data`
  - `base64.verification_type_entree` → `base64._input_type_check`
  - `bdb.definir_trace` → `bdb.set_trace`
  - `bdb.gestionnaire_contexte` → `bdb.contextmanager`
  - `bdb.verifier_nom_fonction` → `bdb.checkfuncname`
  - `bisect.bissection` → `bisect.bisect`
  - `bisect.bissection_droite` → `bisect.bisect_right`
  - `bisect.bissection_gauche` → `bisect.bisect_left`
  - `bisect.insérer_trié` → `bisect.insort`
  - `bisect.insérer_trié_droite` → `bisect.insort_right`
  - `bisect.insérer_trié_gauche` → `bisect.insort_left`
  - `bs4.convertir` → `bs4.cast`
  - `build.verifier_dependance` → `build.check_dependency`
  - `bz2.compresser` → `bz2.compress`
  - `bz2.decompresser` → `bz2.decompress`
  - `bz2.ouvrir` → `bz2.open`
  - `calendrier._longueur_mois` → `calendar._monthlen`
  - `calendrier._mois_precedent` → `calendar._prevmonth`
  - `calendrier._mois_suivant` → `calendar._nextmonth`
  - `calendrier._valider_mois` → `calendar._validate_month`
  - `calendrier.definir_premier_jour_semaine` → `calendar.setfirstweekday`
  - `calendrier.est_bissextile` → `calendar.isleap`
  - `calendrier.formater` → `calendar.format`
  - `calendrier.jour_semaine` → `calendar.weekday`
  - `calendrier.jours_bissextiles` → `calendar.leapdays`
  - `calendrier.longueur_mois` → `calendar._monthlen`
  - `calendrier.mois_precedent` → `calendar._prevmonth`
  - `calendrier.mois_suivant` → `calendar._nextmonth`
  - `calendrier.plage_mois` → `calendar.monthrange`
  - `calendrier.valider_mois` → `calendar._validate_month`
  - `certificats.contenu` → `certifi.contents`
  - `certificats.ou` → `certifi.where`
  - `clic.argument` → `click.argument`
  - `clic.barre_progression` → `click.progressbar`
  - `clic.commande` → `click.command`
  - `clic.confirmer` → `click.confirm`
  - `clic.creer_decorateur_passage` → `click.make_pass_decorator`
  - `clic.demander` → `click.prompt`
  - `clic.echo` → `click.echo`
  - `clic.echo_page` → `click.echo_via_pager`
  - `clic.editer` → `click.edit`
  - `clic.effacer` → `click.clear`
  - `clic.enlever_style` → `click.unstyle`
  - `clic.envelopper_texte` → `click.wrap_text`
  - `clic.formater_nom_fichier` → `click.format_filename`
  - `clic.groupe` → `click.group`
  - `clic.lancer` → `click.launch`
  - `clic.lire_caractere` → `click.getchar`
  - `clic.obtenir_contexte_actuel` → `click.get_current_context`
  - `clic.obtenir_dossier_app` → `click.get_app_dir`
  - `clic.obtenir_flux_binaire` → `click.get_binary_stream`
  - `clic.obtenir_flux_texte` → `click.get_text_stream`
  - `clic.option` → `click.option`
  - `clic.option_aide` → `click.help_option`
  - `clic.option_confirmation` → `click.confirmation_option`
  - `clic.option_mot_de_passe` → `click.password_option`
  - `clic.option_version` → `click.version_option`
  - `clic.ouvrir_fichier` → `click.open_file`
  - `clic.passer_contexte` → `click.pass_context`
  - `clic.passer_objet` → `click.pass_obj`
  - `clic.pause` → `click.pause`
  - `clic.secho` → `click.secho`
  - `clic.style` → `click.style`
  - `code.compiler_commande` → `code.compile_command`
  - `code.interagir` → `code.interact`
  - `codecs.ascii_decoder` → `codecs.ascii_decode`
  - `codecs.ascii_encoder` → `codecs.ascii_encode`
  - `codecs.chercher` → `codecs.lookup`
  - `codecs.chercher_erreur` → `codecs.lookup_error`
  - `codecs.construire_carte_caracteres` → `codecs.charmap_build`
  - `codecs.creer_carte_encodage` → `codecs.make_encoding_map`
  - `codecs.decoder` → `codecs.decode`
  - `codecs.desenregistrer` → `codecs.unregister`
  - `codecs.echappement_decoder` → `codecs.escape_decode`
  - `codecs.echappement_encoder` → `codecs.escape_encode`
  - `codecs.encoder` → `codecs.encode`
  - `codecs.enregistrer` → `codecs.register`
  - `codecs.enregistrer_erreur` → `codecs.register_error`
  - `codecs.erreur_remplacement_barre` → `codecs.backslashreplace_errors`
  - `codecs.erreurs_strictes` → `codecs.strict_errors`
  - `codecs.fichier_encode` → `codecs.EncodedFile`
  - `codecs.ignorer_erreurs` → `codecs.ignore_errors`
  - `codecs.iterer_decoder` → `codecs.iterdecode`
  - `codecs.iterer_encoder` → `codecs.iterencode`
  - `codecs.latin1_decoder` → `codecs.latin_1_decode`
  - `codecs.latin1_encoder` → `codecs.latin_1_encode`
  - `codecs.obtenir_decoder` → `codecs.getdecoder`
  - `codecs.obtenir_ecrivain` → `codecs.getwriter`
  - `codecs.obtenir_encoder` → `codecs.getencoder`
  - `codecs.obtenir_lecteur` → `codecs.getreader`
  - `codecs.ouvrir` → `codecs.open`
  - `codecs.utf8_decoder` → `codecs.utf_8_decode`
  - `codecs.utf8_encoder` → `codecs.utf_8_encode`
  - `codeop._compiler` → `codeop._compile`
  - `codeop._peut_etre_compiler` → `codeop._maybe_compile`
  - `codeop.compiler` → `codeop._compile`
  - `codeop.compiler_commande` → `codeop.compile_command`
  - `codeop.peut_etre_compiler` → `codeop._maybe_compile`
  - `collections._compter_elements` → `collections._count_elements`
  - `collections._est_mot_cle` → `collections._iskeyword`
  - `collections._repr_recursif` → `collections._recursive_repr`
  - `collections.compter_elements` → `collections._count_elements`
  - `collections.est_mot_cle` → `collections._iskeyword`
  - `collections.repr_recursif` → `collections._recursive_repr`
  - `collections.tuple_nomme` → `collections.namedtuple`
  - `colorama.desinit` → `colorama.deinit`
  - `colorama.init` → `colorama.init`
  - `colorama.reinit` → `colorama.reinit`
  - `colorama.reparer_console_windows` → `colorama.just_fix_windows_console`
  - `colorama.texte_couleur` → `colorama.colorama_text`
  - `comparaison_fichier.comparer` → `filecmp.cmp`
  - `comparaison_fichier.comparer_fichiers` → `filecmp.cmpfiles`
  - `comparaison_fichier.vider_cache` → `filecmp.clear_cache`
  - `contexte.envelopper` → `contextlib.wraps`
  - `contexte.gestionnaire` → `contextlib.contextmanager`
  - `contexte.gestionnaire_async` → `contextlib.asynccontextmanager`
  - `contour.calculer_tailles_blocs` → `contourpy.calc_chunk_sizes`
  - `contour.convertir_lignes` → `contourpy.convert_lines`
  - `contour.convertir_rempli` → `contourpy.convert_filled`
  - `contour.generateur_contour` → `contourpy.contour_generator`
  - `copie._copie_profonde_dict` → `copy._deepcopy_dict`
  - `copie._copie_profonde_liste` → `copy._deepcopy_list`
  - `copie.copie_profonde` → `copy.deepcopy`
  - `copie.copie_profonde_dict` → `copy._deepcopy_dict`
  - `copie.copie_profonde_liste` → `copy._deepcopy_list`
  - `copie.copier` → `copy.copy`
  - `copie.remplacer` → `copy.replace`
  - `correspondance.filtrer` → `fnmatch.filter`
  - `correspondance.fnmatch` → `fnmatch.fnmatch`
  - `correspondance.traduire` → `fnmatch.translate`
  - `couleurs.hls_vers_rgb` → `colorsys.hls_to_rgb`
  - `couleurs.hsv_vers_rgb` → `colorsys.hsv_to_rgb`
  - `couleurs.rgb_vers_hls` → `colorsys.rgb_to_hls`
  - `couleurs.rgb_vers_hsv` → `colorsys.rgb_to_hsv`
  - `csv.desenregistrer_dialecte` → `csv.unregister_dialect`
  - `csv.ecrivain` → `csv.writer`
  - `csv.enregistrer_dialecte` → `csv.register_dialect`
  - `csv.lecteur` → `csv.reader`
  - `csv.limite_taille_champ` → `csv.field_size_limit`
  - `csv.lister_dialectes` → `csv.list_dialects`
  - `csv.obtenir_dialecte` → `csv.get_dialect`
  - `ctypes.ErreurFormat` → `ctypes.FormatError`
  - `ctypes.ErreurWin` → `ctypes.WinError`
  - `ctypes.POINTEUR` → `ctypes.POINTER`
  - `ctypes.TABLEAU` → `ctypes.ARRAY`
  - `ctypes._charger_bibliotheque` → `ctypes._LoadLibrary`
  - `ctypes.adresse_de` → `ctypes.addressof`
  - `ctypes.alignement` → `ctypes.alignment`
  - `ctypes.chaine_a` → `ctypes.string_at`
  - `ctypes.chaine_large_a` → `ctypes.wstring_at`
  - `ctypes.charger_bibliotheque` → `ctypes._LoadLibrary`
  - `ctypes.convertir` → `ctypes.cast`
  - `ctypes.creer_tampon_chaine` → `ctypes.create_string_buffer`
  - `ctypes.creer_tampon_unicode` → `ctypes.create_unicode_buffer`
  - `ctypes.obtenir_derniere_erreur` → `ctypes.get_last_error`
  - `ctypes.obtenir_errno` → `ctypes.get_errno`
  - `ctypes.par_ref` → `ctypes.byref`
  - `ctypes.pointeur` → `ctypes.pointer`
  - `ctypes.redimensionner` → `ctypes.resize`
  - `ctypes.taille_de` → `ctypes.sizeof`
  - `ctypes.tampon_c` → `ctypes.c_buffer`
  - `ctypes.vue_memoire_a` → `ctypes.memoryview_at`
  - `cycleur.ajouter` → `cycler.add`
  - `cycleur.concatener` → `cycler.concat`
  - `cycleur.cycleur` → `cycler.cycler`
  - `cycleur.multiplier` → `cycler.mul`
  - `cycleur.reduire` → `cycler.reduce`
  - `dbm.ouvrir` → `dbm.open`
  - `dbm.quel_db` → `dbm.whichdb`
  - `decimal.contexte_local` → `decimal.localcontext`
  - `decimal.definir_contexte` → `decimal.setcontext`
  - `decimal.obtenir_contexte` → `decimal.getcontext`
  - `diff._calculer_ratio` → `difflib._calculate_ratio`
  - `diff.calculer_ratio` → `difflib._calculate_ratio`
  - `diff.diff_contexte` → `difflib.context_diff`
  - `diff.diff_unifie` → `difflib.unified_diff`
  - `diff.obtenir_correspondances_proches` → `difflib.get_close_matches`
  - `diff.restaurer` → `difflib.restore`
  - `dill.charger` → `dill.load`
  - `dill.charger_module` → `dill.load_module`
  - `dill.charger_session` → `dill.load_session`
  - `dill.copier` → `dill.copy`
  - `dill.sauvegarder` → `dill.dump`
  - `dill.sauvegarder_module` → `dill.dump_module`
  - `dill.sauvegarder_session` → `dill.dump_session`
  - `dill.verifier` → `dill.check`
  - `dis._desassembler_octets` → `dis._disassemble_bytes`
  - `dis._trouver_importations` → `dis._find_imports`
  - `dis.analyser` → `dis.dis`
  - `dis.desassembler` → `dis.disassemble`
  - `dis.desassembler_octets` → `dis._disassemble_bytes`
  - `dis.effet_pile` → `dis.stack_effect`
  - `dis.info_code` → `dis.code_info`
  - `dis.instructions` → `dis.get_instructions`
  - `dis.montrer_code` → `dis.show_code`
  - `dis.trouver_importations` → `dis._find_imports`
  - `django.configuration` → `django.setup`
  - `django.obtenir_version` → `django.get_version`
  - `doctest._indenter` → `doctest._indent`
  - `doctest._tester` → `doctest._test`
  - `doctest.deboguer` → `doctest.debug`
  - `doctest.exemples_vers_script` → `doctest.script_from_examples`
  - `doctest.indenter` → `doctest._indent`
  - `doctest.source_test` → `doctest.testsource`
  - `doctest.tester` → `doctest._test`
  - `doctest.tester_fichier` → `doctest.testfile`
  - `doctest.tester_module` → `doctest.testmod`
  - `donnees._en_dict_interne` → `dataclasses._asdict_inner`
  - `donnees.champ` → `dataclasses.field`
  - `donnees.champs` → `dataclasses.fields`
  - `donnees.creer_donnee_classe` → `dataclasses.make_dataclass`
  - `donnees.donnee_classe` → `dataclasses.dataclass`
  - `donnees.en_dict` → `dataclasses.asdict`
  - `donnees.en_dict_interne` → `dataclasses._asdict_inner`
  - `donnees.en_tuple` → `dataclasses.astuple`
  - `donnees.est_donnee_classe` → `dataclasses.is_dataclass`
  - `donnees.remplacer` → `dataclasses.replace`
  - `email.message_depuis_chaine` → `email.message_from_string`
  - `email.message_depuis_fichier` → `email.message_from_file`
  - `email.message_depuis_fichier_binaire` → `email.message_from_binary_file`
  - `email.message_depuis_octets` → `email.message_from_bytes`
  - `encodage.definir_journalisation` → `charset_normalizer.set_logging_handler`
  - `encodage.depuis_chemin` → `charset_normalizer.from_path`
  - `encodage.depuis_octets` → `charset_normalizer.from_bytes`
  - `encodage.detecter` → `charset_normalizer.detect`
  - `encodage.est_binaire` → `charset_normalizer.is_binary`
  - `encodages.normaliser_encodage` → `encodings.normalize_encoding`
  - `encodages.rechercher_fonction` → `encodings.search_function`
  - `ensurepip._amorce` → `ensurepip._bootstrap`
  - `ensurepip.amorce` → `ensurepip.bootstrap`
  - `ensurepip.version` → `ensurepip.version`
  - `entree_fichier.entree` → `fileinput.input`
  - `entree_fichier.fermer` → `fileinput.close`
  - `entree_fichier.fichier_suivant` → `fileinput.nextfile`
  - `entree_fichier.nom_fichier` → `fileinput.filename`
  - `entree_fichier.num_ligne` → `fileinput.lineno`
  - `enum._est_prive` → `enum._is_private`
  - `enum.afficher_valeurs_drapeau` → `enum.show_flag_values`
  - `enum.est_prive` → `enum._is_private`
  - `enum.unique` → `enum.unique`
  - `flask.apres_cette_requete` → `flask.after_this_request`
  - `flask.avorter` → `flask.abort`
  - `flask.creer_reponse` → `flask.make_response`
  - `flask.envoyer_depuis_dossier` → `flask.send_from_directory`
  - `flask.envoyer_fichier` → `flask.send_file`
  - `flask.flasher` → `flask.flash`
  - `flask.jsonnifier` → `flask.jsonify`
  - `flask.obtenir_messages_flash` → `flask.get_flashed_messages`
  - `flask.rediriger` → `flask.redirect`
  - `flask.rendre_chaine_modele` → `flask.render_template_string`
  - `flask.rendre_modele` → `flask.render_template`
  - `flask.url_pour` → `flask.url_for`
  - `flux.analyser` → `feedparser.parse`
  - `flux.enregistrer_gestionnaire_date` → `feedparser.registerDateHandler`
  - `fonctions._trouver_impl` → `functools._find_impl`
  - `fonctions.cache` → `functools.cache`
  - `fonctions.dispatch_unique` → `functools.singledispatch`
  - `fonctions.envelopper` → `functools.wraps`
  - `fonctions.lru_cache` → `functools.lru_cache`
  - `fonctions.mise_a_jour_enveloppe` → `functools.update_wrapper`
  - `fonctions.ordre_total` → `functools.total_ordering`
  - `fonctions.reduire` → `functools.reduce`
  - `fonctions.trouver_impl` → `functools._find_impl`
  - `fonctions.wraps` → `functools.wraps`
  - `fractions._arrondir_exposant` → `fractions._round_to_exponent`
  - `fractions.arrondir_exposant` → `fractions._round_to_exponent`
  - `frython.transpileur` → `frython.transpiler`
  - `fsspec.compressions_disponibles` → `fsspec.available_compressions`
  - `fsspec.enregistrer_implementation` → `fsspec.register_implementation`
  - `fsspec.ouvrir` → `fsspec.open`
  - `fsspec.ouvrir_fichiers` → `fsspec.open_files`
  - `fsspec.protocoles_disponibles` → `fsspec.available_protocols`
  - `fsspec.systeme_fichiers` → `fsspec.filesystem`
  - `functorch.grad` → `functorch.grad`
  - `functorch.hessienne` → `functorch.hessian`
  - `functorch.rendre_fonctionnel` → `functorch.make_functional`
  - `functorch.vmap` → `functorch.vmap`
  - `jeux_donnees.activer_barre_progression` → `datasets.enable_progress_bar`
  - `jeux_donnees.activer_cache` → `datasets.enable_caching`
  - `jeux_donnees.charger` → `datasets.load_dataset`
  - `jeux_donnees.charger_depuis_disque` → `datasets.load_from_disk`
  - `jeux_donnees.concatener` → `datasets.concatenate_datasets`
  - `jeux_donnees.desactiver_barre_progression` → `datasets.disable_progress_bar`
  - `jeux_donnees.desactiver_cache` → `datasets.disable_caching`
  - `jeux_donnees.entrelacer` → `datasets.interleave_datasets`
  - `profiler.etiquette` → `cProfile.label`
  - `profiler.lancer` → `cProfile.run`
  - `profiler.lancer_contexte` → `cProfile.runctx`
  - `registre_copie.ajouter_extension` → `copyreg.add_extension`
  - `registre_copie.constructeur` → `copyreg.constructor`
  - `registre_copie.supprimer_extension` → `copyreg.remove_extension`
  - `tout_compiler.compiler_chemin` → `compileall.compile_path`
  - `tout_compiler.compiler_dossier` → `compileall.compile_dir`
  - `tout_compiler.compiler_fichier` → `compileall.compile_file`
  - `variables_contexte.copier_contexte` → `contextvars.copy_context`

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
