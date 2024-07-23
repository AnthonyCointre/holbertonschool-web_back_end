0-get_list_students.js = Une fonction nommée getListStudents qui renvoie un tableau d'objets. Chaque objet doit avoir trois attributs : id (Nombre), firstName (Chaîne) et location (Chaîne).

1-get_list_student_ids.js = Une fonction getListStudentIds qui renvoie un tableau d'identifiants à partir d'une liste d'objets. Cette fonction prend un argument qui est un tableau d'objets - et ce tableau a le même format que getListStudents de la tâche précédente. Si l'argument n'est pas un tableau, la fonction renvoie un tableau vide. Utiliser la fonction map sur le tableau.

2-get_students_by_loc.js = Une fonction getStudentsByLocation qui renvoie un tableau d'objets situés dans une ville spécifique. Il doit accepter une liste d'étudiants (de getListStudents) et une ville (chaîne) comme paramètres. Utiliser la fonction filter sur le tableau.

3-get_ids_sum.js = Une fonction getStudentIdsSum qui renvoie la somme de tous les identifiants des étudiants. Il doit accepter une liste d'étudiants (de getListStudents) comme paramètre. Utiliser la fonction reduce sur le tableau.

4-update_grade_by_city.js = Une fonction updateStudentGradeByCity qui renvoie un tableau d'étudiants pour une ville spécifique avec leur nouvelle note Il doit accepter une liste d'étudiants (de getListStudents), une ville (Chaîne) et newGrades (Tableau d'objets « grade ») comme paramètres. Si un élève n’a pas de note dans newGrades, la note finale doit être N/A. Utiliser filter et map combinés.

5-typed_arrays.js = Une fonction nommée createInt8TypedArray qui renvoie un nouveau ArrayBuffer avec une valeur Int8 à une position spécifique. Il doit accepter trois arguments : length (Nombre), position (Nombre), and value (Nombre) Si l’ajout de la valeur n’est pas possible, l’erreur Position hors plage doit être générée.

6-set.js = Une fonction nommée setFromArray qui renvoie un Set à partir d'un tableau. Il accepte un argument (Array, de tout type d'élément).

7-has_array_values.js = Une fonction nommée hasValuesFromArray qui renvoie un booléen si tous les éléments du tableau existent dans l'ensemble. Il accepte deux arguments : un set (Ensemble) et un array (Tableau).

8-clean_set.js = Une fonction nommée cleanSet qui renvoie une chaîne de toutes les valeurs définies commençant par une chaîne spécifique (startString). Il accepte deux arguments : un set (Ensemble) et un startString (Chaîne). Lorsqu'une valeur commence par startString, vous ajoutez uniquement le reste de la chaîne. La chaîne contient toutes les valeurs de l'ensemble séparées par -.

9-groceries_list.js = Une fonction nommée groceriesList qui renvoie une carte des courses avec les éléments suivants (nom, quantité)

10-update_uniq_items.js = Une fonction nommée updateUniqueItems qui renvoie une carte mise à jour pour tous les éléments dont la quantité initiale est de 1. Elle doit accepter une carte comme argument. La carte qu'il accepte comme argument est similaire à la carte que vous créez dans la tâche précédente. Pour chaque entrée de la carte où la quantité est 1, mettez à jour la quantité à 100. Si la mise à jour de la quantité n'est pas possible (l'argument n'est pas une carte), l'erreur Cannot process doit être générée.
