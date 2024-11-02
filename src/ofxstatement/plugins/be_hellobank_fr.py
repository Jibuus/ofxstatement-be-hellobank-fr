# This file is part of ofxstatement-be-hellobank-fr.
#
# ofxstatement-be-hellobank-fr is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ofxstatement-be-hellobank-fr is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ofxstatement-be-hellobank-fr.  If not, see <https://www.gnu.org/licenses/>.


from ofxstatement.plugin import Plugin
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import StatementLine, Statement
from datetime import datetime
import csv

class HelloBankFRPlugin(Plugin):
    """Plugin for HelloBank CSV files."""
    # Plugin pour les fichiers CSV de la banque HelloBank.

    def get_parser(self, filename):
        # Return the parser for the HelloBank CSV file.
        # Retourne le parser pour le fichier CSV de HelloBank.
        return HelloBankFRParser(filename)

class HelloBankFRParser(CsvStatementParser):
    date_format = "%d/%m/%Y"
    # Date format used in the CSV file (DD/MM/YYYY).
    # Format de date utilisé dans le fichier CSV (JJ/MM/AAAA).

    def __init__(self, filename):
        super().__init__(filename)
        self.statement = Statement()
        # Initialize a new statement object to hold the parsed data.
        # Initialise un nouvel objet de relevé pour stocker les données analysées.

    def split_payee(self, row):
        # Concatenate payee details according to the user specifications
        # Concaténer les détails du bénéficiaire selon les spécifications.
        return " - ".join([
            row.get("Contrepartie", "").strip(),
            row.get("Nom de la contrepartie", "").strip(),
        ]).replace(" -  - ", " - ")

    def split_memo(self, row):
        # Concatenate memo details from different fields in the CSV
        # Concaténer les détails de la communication à partir de plusieurs champs du CSV.
        return " - ".join([
            row.get("Détails", "").strip(),
            row.get("Communication", "").strip(),
        ]).replace(" -  - ", " - ")

    def parse_movement_type(self, type_movement):
        # Map CSV transaction types to OFX transaction types.
        # Associer les types de transactions du CSV aux types de transactions OFX.
        mapping = {
            "Paiement par carte": "POS",  # Point of Sale transaction / Paiement par carte
            "Virement instantané en euros": "XFER",  # Transfer / Virement instantané
        }
        return mapping.get(type_movement, "OTHER")  # Default to "OTHER" if not mapped / Défaut "AUTRE"

    def parse(self):
        # Initialize statement currency to EUR / Initialiser la devise du relevé en EUR.
        self.statement.currency = "EUR"
        
        with open(self.fin, newline="", encoding="utf-8-sig") as csvfile:
            # Open the CSV file with UTF-8 encoding / Ouvrir le fichier CSV avec l'encodage UTF-8.
            reader = csv.DictReader(csvfile, delimiter=";", skipinitialspace=True)
            # Use DictReader to parse the CSV rows as dictionaries / Utiliser DictReader pour analyser les lignes du CSV sous forme de dictionnaires.

            for row in reader:
                # Set the account ID from the CSV / Définir l'ID du compte à partir du CSV.
                self.statement.account_id = row["Numéro de compte"].strip()

                line = StatementLine()  # Create a new statement line / Créer une nouvelle ligne de relevé.
                
                # Parse the execution date / Analyser la date d'exécution.
                line.date = datetime.strptime(row["Date d'exécution"], self.date_format)

                # Parse the transaction ID / Analyser l'identifiant de la transaction.
                line.id = row["Nº de séquence"]

                # Concatenate payee details / Concaténer les détails du bénéficiaire.
                line.payee = self.split_payee(row)

                # Parse the memo field / Analyser le champ de communication.
                line.memo = self.split_memo(row)

                # Parse the amount and convert it to float / Analyser le montant et le convertir en float.
                line.amount = float(row["Montant"].replace(",", "."))

                # Parse the transaction type / Analyser le type de transaction.
                line.trntype = self.parse_movement_type(row["Type de transaction"])

                # Add the transaction line to the statement / Ajouter la ligne de relevé à la liste.
                self.statement.lines.append(line)

        return self.statement  # Return the parsed statement / Retourner le relevé analysé.
