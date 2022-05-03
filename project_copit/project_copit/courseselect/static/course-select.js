const courses = document.querySelectorAll('.course')
const semesters = document.querySelectorAll('.semester')
const courseSelection = document.querySelectorAll('.bigContainer')

courses.forEach(course => {
    course.addEventListener('dragstart', () => {
        course.classList.add('dragging')
    })
    course.addEventListener('dragend', () => {
        course.ClassList.remove('dragging')
    })
});

semesters.forEach(semester => {
    semester.addEventListener('dragover', e => {
        e.preventDefault()
        console.log('dragging over')
        const course = document.querySelector('.dragging')
        semester.appendChild(course)
    })
})

courseSelection.forEach(bigContainer => {
    bigContainer.addEventListener('dragover', e => {
        e.preventDefault()
        console.log('dragging over')
        const course = document.querySelector('.dragging')
        bigContainer.appendChild(course)
    })
})