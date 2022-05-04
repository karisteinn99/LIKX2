const courses = document.querySelectorAll('.course')
const semesters = document.querySelectorAll('.semester')
const courseSelection = document.querySelectorAll('.bigContainer')

courses.forEach(course => {
    course.addEventListener('dragstart', () => {
        course.classList.add('dragging')
    })
    course.addEventListener('dragend', () => {
        course.classList.remove('dragging')
    })
});

semesters.forEach(semester => {
    semester.addEventListener('dragover', e => {
      e.preventDefault()
      const afterElement = getDragAfterElement(semester, e.clientY)
      const draggable = document.querySelector('.dragging')
      if (afterElement == null) {
        semester.appendChild(draggable)
      } else {
        semester.insertBefore(draggable, afterElement)
      }
    })
  })

  courseSelection.forEach(bigContainer => {
    bigContainer.addEventListener('dragover', e => {
      e.preventDefault()
      const afterElement = getDragAfterElement(bigContainer, e.clientY)
      const draggable = document.querySelector('.dragging')
      if (afterElement == null) {
        bigContainer.appendChild(draggable)
      } else {
        bigContainer.insertBefore(draggable, afterElement)
      }
    })
  })
  
  function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll('.draggable:not(.dragging)')]
    return draggableElements.reduce((closest, child) => {
      const box = child.getBoundingClientRect()
      const offset = y - box.top - box.height / 2
      console.log(offset)
      if (offset < 0 && offset > closest.offset) {
        return { offset: offset, element: child }
      } else {
        return closest
      }
    }, { offset: Number.POSITIVE_INFINITY }).element
  }


