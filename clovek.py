class Clovek:
    """
    Třída reprezentuje člověka, která má jméno, věk a kamaráda
    """
    # atributy
    jmeno = None
    vek = None
    kamarad = None

    # metody
    def predstav_se(self):
        print("Ahoj, já jsem {0}, \
je mi {1} let \
a můj kamarád je {2}"
              .format(self.jmeno,
                      self.vek,
                      self.kamarad.jmeno))
