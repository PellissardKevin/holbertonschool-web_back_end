export default function updateStudentGradeByCity(students, city, newGrades) {
  const result = students
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.filter((newGrade) => newGrade.studentId === student.id);
      return { ...student, grade: grade.length ? grade[0].grade : 'N/A' };
    });
  return result;
}
