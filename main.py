from clovek import Clovek

# Vytvoření lidí (instancí)
karel = Clovek()
karel.jmeno = "Karel Novák"
karel.vek = 33
josef = Clovek()
josef.jmeno = "Cyril Nový"
josef.vek = 27

# Spřátelení
karel.kamarad = josef
josef.kamarad = karel

# Představení
karel.predstav_se()
josef.predstav_se()
