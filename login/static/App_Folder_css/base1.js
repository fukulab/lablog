// script.js
console.log('JavaScriptファイルが読み込まれました');
var buttons = document.querySelectorAll('.btn');
console.log(buttons.length);
buttons.forEach(button => {
    console.log(1)
	button.addEventListener('click', () => {
		const links = button.parentNode.querySelectorAll('a');
		links.forEach(link => {
			link.classList.toggle('show');
		});
	});
});
