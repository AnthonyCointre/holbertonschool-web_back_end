0-constants.js = modifier la fonction taskFirst pour instancier les variables à l'aide de const et la fonction taskNext pour instancier les variables à l'aide de let.

1-block-scoped.js = modifier les variables à l'intérieur de la fonction taskBlock afin que les variables ne soient pas écrasées à l'intérieur du bloc conditionnel.

2-arrow.js = réécrire la fonction standard suivante pour utiliser la syntaxe de flèche d'ES6 de la fonction add (ce sera une fonction anonyme après).

3-default-parameter.js = condenser les éléments internes de la fonction suivante sur 1 ligne - sans changer le nom de chaque fonction/variable.

4-rest-parameter.js = modifier la fonction pour renvoyer le nombre d'arguments qui lui sont transmis en utilisant la syntaxe du paramètre rest.

5-spread-operator.js = en utilisant la syntaxe spread, concaténer 2 tableaux et chaque caractère d'une chaîne en modifiant la fonction ci-dessous. Le corps de la fonction doit comporter une seule ligne. export default function concatArrays(array1, array2, string) {}

6-string-interpolation.js = réécrire l'instruction return pour utiliser un modèle littéral afin de pouvoir remplacer les variables que vous avez définies.

7-getBudgetObject.js = modifier l'objet budget de la fonction suivante pour utiliser simplement la syntaxe abrégée de la valeur de la propriété de l'objet à la place.

8-getBudgetCurrentYear.js = réécrire la fonction getBudgetForCurrentYear pour utiliser les noms de propriétés calculés ES6 sur l'objet budgétaire.

9-getFullBudget.js = réécrire getFullBudgetObject pour utiliser les propriétés de la méthode ES6 dans l'objet fullBudget.

10-loops.js = réécrire la fonction appendToEachArrayValue pour utiliser l'opérateur for...of d'ES6. Et n'oubliez pas que var n'est pas compatible ES6.

11-createEmployeesObject.js = écrire une fonction nommée createEmployeesObject qui recevra deux arguments : departmentName (String) employees (Array of Strings)

12-createReportObject.js = écrire une fonction nommée createReportObject dont le paramètre, EmployeesList, est la valeur de retour de la fonction précédente createEmployeesObject. exporter la fonction par défaut createReportObject (employeesList) {} createReportObject doit renvoyer un objet contenant la clé allEmployees et une propriété de méthode appelée getNumberOfDepartments. allEmployees est une clé qui correspond à un objet contenant le nom du service et une liste de tous les employés de ce service. Si vous rencontrez des problèmes, utilisez la syntaxe spread. La propriété méthode reçoit EmployeesList et renvoie le nombre de départements.
