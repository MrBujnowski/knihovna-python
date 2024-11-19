import csv
import json
from tabulate import tabulate


class KnihovniSystem:
    def __init__(self, nazev_souboru):
        self.soubor = nazev_souboru
        self.knihy = self.nacti_knihy()

    def nacti_knihy(self):
        try:
            with open(self.soubor, 'r', encoding='utf8') as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            print('Soubor left the channel')
        except:
            print('Stalo se cosi divného')
        finally:
            pass

    # def uloz_knihy(self):
    #     pass

    # def import_json(self, json_soubor):
    #     pass



    def uloz_knihy(self):
        if self.knihy:
            fieldnames = self.knihy[0].keys()
            try:
                with open(self.soubor, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.knihy)
            except FileNotFoundError:
                print(f'Soubor {self.soubor} nebyl nalezen')


    def import_json(self, json_soubor):
        try:
            with open(json_soubor, 'r', encoding='utf-8') as f:
                knihy = json.load(f)
                self.knihy = knihy
                self.uloz_knihy()
                print('Knihy byly uspesne importovany')
        except FileNotFoundError:
            print(f'Soubor {json_soubor} nebyl nalezen')



    def export_json(self, json_soubor):
        try:
            with open(json_soubor, 'x', encoding='utf-8') as f:
                f.write(json.dumps(self.knihy, indent=4))
        except FileExistsError:
            print('Soubor left the channel')
        except:
            print('Stalo se cosi divného')
        return []

    def zobraz_knihy(self):
        if not self.knihy:
            print('Nejsou žádné knihy k dispozicic')
            return

        header = {
            'isbn': 'ISBN',
            'nazev_knihy': 'Název knihy',
            'autor': 'Autor',
            'pocet_stran': 'Počet stran',
            'zanr': 'Žánr',
            'rok_vydani': 'Rok vydání',
            'nakladatelstvi': 'Nakladatelství',
            'cena': 'Cena'
        }


system = KnihovniSystem('knihy.csv')
system.knihy[0]['pocet_stran'] = 1
system.uloz_knihy()
system.import_json('knihy.json')
print(system.knihy[0]['nazev_knihy'])