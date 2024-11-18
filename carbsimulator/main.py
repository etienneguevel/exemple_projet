import random

def calculate():
    """
    CECI EST UN EXEMPLE, VOUS POUVEZ VOUS EN INSPIRER OU FAIRE TOTALEMENT AUTREMENT.
    
    """
    questions = {
        "nourriture": {
            "legume": "Combien de kg de légumes avez-vous utilisé ?\n",
            "boeuf": "Combien de kg de boeuf avez-vous utilisé ?\n",
            "viande": "Combien de kg d'autres viandes avez-vous utilisé ?\n",
            "alcool": "Combien de litres de boissons alcoolisées avez-vous servis ?\n",
            "sodas": 
                "Combien de litres de boissons non-alcoolisées"\
                "(autre que de l'eau) avez-vous servis ?\n",
        },
        "energie": {
            "type": 
            "Quel type d'énergie utilisez-vous"\
            "(écrire : fioul, gaz, granules, electricite) ?\n",
            "qty": "Quantite (en kWh) ?"
        },
    }

    while True:
        choice = input(
            "Quelle type d'évaluation souhaitez vous faire"\
            "(écrire : hebdomadaire, mensuelle ou annuelle) ?\n"
        )
        if choice in ["hebdomadaire", "mensuelle", "annuelle"]:
            break

        print("Indiquez une réponse dans celles proposées.")

    for ty in questions:
        print(f"\n\nCatégorie : {ty}")
        for subty in questions.get(ty):
            input(questions.get(ty).get(subty))

    print("\n\n")
    print("CE PROGRAMME EST UN EXEMPLE, LES VALEURS SONT ARBITRAIRES")
    print("\n\n")
    carbone_empreinte = random.uniform(2, 10)
    print(f"Votre empreinte carbone {choice} est de {carbone_empreinte:.1f} tonnes")

    print("\n\nDétails")
    ratio = random.uniform(0.25, 0.75)
    print(f"Alimentation : {carbone_empreinte*ratio:.1f} t")
    print(f"Energie : {carbone_empreinte*(1-ratio):.1f} t")

if __name__ == "__main__":
    calculate()
