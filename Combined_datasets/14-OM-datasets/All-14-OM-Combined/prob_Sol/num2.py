class BooleanFormula:
    def __init__(self, formula):
        self.formula = formula

    def transform_to_cnf(self):
        self.apply_demorgan()
        self.eliminate_implication()
        self.distribute_conjunction()
        cnf = self.convert_to_cnf()
        return cnf

    def apply_demorgan(self):
        self.formula = self._apply_demorgan_recursively(self.formula)

    def _apply_demorgan_recursively(self, subformula):
        if isinstance(subformula, str):
            return subformula
        elif subformula[0] == '¬':
            operator = subformula[0]
            operand = subformula[1]
            if isinstance(operand, str):
                return subformula
            elif operand[0] == '∧':
                return ['∨', self._apply_demorgan_recursively(['¬', operand[1]]), self._apply_demorgan_recursively(['¬', operand[2]])]
            elif operand[0] == '∨':
                return ['∧', self._apply_demorgan_recursively(['¬', operand[1]]), self._apply_demorgan_recursively(['¬', operand[2]])]
        elif subformula[0] == '∧' or subformula[0] == '∨':
            operator = subformula[0]
            operand1 = self._apply_demorgan_recursively(subformula[1])
            operand2 = self._apply_demorgan_recursively(subformula[2])
            return [operator, operand1, operand2]

    def eliminate_implication(self):
        self.formula = self._eliminate_implication_recursively(self.formula)

    def _eliminate_implication_recursively(self, subformula):
        if isinstance(subformula, str):
            return subformula
        elif subformula[0] == '→':
            operand1 = self._eliminate_implication_recursively(['¬', subformula[1]])
            operand2 = self._eliminate_implication_recursively(subformula[2])
            return ['∨', operand1, operand2]
        elif subformula[0] == '∧' \or subformula[0] == '∨':
            operator = subformula[0]
            operand1 = self._eliminate_implication_recursively(subformula[1])
            operand2 = self._eliminate_implication_recursively(subformula[2])
            return [operator, operand1, operand2]

    def distribute_conjunction(self):
        self.formula = self._distribute_conjunction_recursively(self.formula)

    def _distribute_conjunction_recursively(self, subformula):
        if isinstance(subformula, str):
            return subformula
        elif subformula[0] == '∧':
            operand1 = self._distribute_conjunction_recursively(subformula[1])
            operand2 = self._distribute_conjunction_recursively(subformula[2])
            if operand1[0] == '∨':
                return ['∨', self._distribute_conjunction_recursively(['∧', operand1[1], operand2]), self._distribute_conjunction_recursively(['∧', operand1[2], operand2])]
            elif operand2[0] == '∨':
                return ['∨', self._distribute_conjunction_recursively(['∧', operand1, operand2[1]]), self._distribute_conjunction_recursively(['∧', operand1, operand2[2]])]
        elif subformula[0] == '∧' or
