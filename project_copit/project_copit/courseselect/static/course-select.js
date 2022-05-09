const courses = document.querySelectorAll('.course')
const semesters = document.querySelectorAll('.semester')
const courseSelection = document.querySelectorAll('.bigContainer')

// draggable elements and stuff around that
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
    }, { offset: Number.NEGATIVE_INFINITY }).element
  }

// this changes description text (course.description outer html) to the correct format 
const descriptions = document.querySelectorAll('.destringify')
descriptions.forEach(description => {
  string_1 = description.outerHTML.replaceAll('&lt;', '<')
  string_2 = string_1.replaceAll('&gt;', '>')
  string_3 = string_2.replaceAll('&amp;nbsp;', ' ')
  description.outerHTML = string_3
})

// info popup window
function openInfo(id) {
  document.getElementById(id).style.display = "block";
  courses.forEach(course => {
    course.setAttribute("draggable", false)
  })
}

function closeInfo(id) {
  document.getElementById(id).style.display = "none";
  courses.forEach(course => {
    course.setAttribute("draggable", true)
  })
}

function form_function() {
  i = 1
  semesters.forEach (semester => {
    s_value = ''
    semester.childNodes.forEach(course => {
      course_id = course.getAttribute('class').split(' ')[1]
      s_value = s_value + course_id + ' ' 
      console.log(s_value)
      form_input = document.getElementById('semester-'+ i)
      form_input.setAttribute('value', s_value)
    })
    console.log(s_value)
    i = i + 1
  })
}


