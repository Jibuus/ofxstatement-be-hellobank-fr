
**Note:** The English version is presented first, followed by the French version.

ofxstatement-be-hellobank-fr Plugin for ofxstatement
====================================================

This project provides an ofxstatement plugin to convert CSV bank statements from the Belgian bank Hellobank into OFX format.

ofxstatement is a tool for converting proprietary bank statements to OFX format, suitable for importing into financial management software like Skrooge. The ofxstatement plugin parses a specific proprietary bank statement format and produces a common data structure, which is then formatted into an OFX file.

Several ofxstatement users have developed plugins for their banks. These plugins are listed on the main ofxstatement website.

Installation and Usage
----------------------

To install **ofxstatement** and the necessary plugin, please refer to the ofxstatement GitHub page: https://github.com/kedder/ofxstatement

Usage
-----

To convert a proprietary `hellobank.csv` file into an OFX file, use the following command:

.. code-block:: shell

    ofxstatement convert -t be_hellobank_fr hellobank.csv hellobank.ofx

Command explanation:
- ``-t be_hellobank_fr``: Specifies the Hellobank plugin to use for the conversion.
- ``hellobank.csv``: The CSV file provided by the Hellobank bank.
- ``hellobank.ofx``: The generated OFX file.

Credits
-------

This project builds upon the work of Kedder, the creator of ofxstatement (https://github.com/kedder/ofxstatement). Thanks to Kedder for making this tool available and for providing a foundation for various bank plugins, including this one.

License
-------

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

Plugin ofxstatement-be-hellobank-fr pour ofxstatement
=====================================================

Ce projet fournit un plugin ofxstatement pour convertir les relevés bancaires au format CSV de la banque belge Hellobank en format OFX.

ofxstatement est un outil permettant de convertir les relevés bancaires propriétaires au format OFX, adapté pour l'importation dans des logiciels de gestion financière comme Skrooge. Le plugin ofxstatement analyse un format de relevé bancaire propriétaire spécifique et produit une structure de données commune, qui est ensuite formatée en fichier OFX.

Plusieurs utilisateurs d'ofxstatement ont développé des plugins pour leurs banques. Ces plugins sont listés sur le site principal d'ofxstatement.

Installation et utilisation
---------------------------

Pour installer **ofxstatement** et le plugin nécessaire, veuillez consulter la page GitHub de ofxstatement: https://github.com/kedder/ofxstatement

Utilisation
-----------

Pour convertir un fichier propriétaire ``hellobank.csv`` en fichier OFX, utilisez la commande suivante :

.. code-block:: shell

    ofxstatement convert -t be_hellobank_fr hellobank.csv hellobank.ofx

Explication de la commande :
- ``-t be_hellobank_fr`` : Spécifie le plugin Hellobank à utiliser pour la conversion.
- ``hellobank.csv`` : Le fichier CSV fourni par la banque Hellobank.
- ``hellobank.ofx`` : Le fichier OFX qui sera généré.

Crédits
-------

Ce projet s'appuie sur le travail de Kedder, le créateur de ofxstatement (https://github.com/kedder/ofxstatement). Merci à Kedder pour avoir rendu cet outil disponible et pour avoir fourni une base pour divers plugins bancaires, y compris celui-ci.

Licence
-------

Ce projet est sous licence GNU General Public License v3.0. Voir le fichier LICENSE pour plus de détails.
