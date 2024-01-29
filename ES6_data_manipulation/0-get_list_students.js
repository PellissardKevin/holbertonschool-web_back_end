export default function getListStudents() {
	let listStudents = ["1,Guillaume,San Francisco",
		"2,James,Columbia",
		"5,Serena,San Francisco"
	];
	let deck = [];

	for (let i = 0; i < listStudents.length; i++) {
		const listStudentsArray = listStudents[i].split(',');
		const id = parseInt(listStudentsArray[0]);
		const firstName = listStudentsArray[1];
		const location = listStudentsArray[2];
		deck.push({ id, firstName, location });
	}
	return deck;
};
