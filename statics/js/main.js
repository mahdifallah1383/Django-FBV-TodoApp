const taskInput = document.getElementById("taskInput");
const addButton = document.getElementById("addButton");
const tasksContainer = document.getElementById("tasksContainer");

// Add new task
function addTask() {
  const title = taskInput.value.trim();

  if (title === "") {
    return;
  }

  const task = document.createElement("div");
  task.classList.add("task");

  task.innerHTML = `
                <div class="task-content">

                    <input
                        type="radio"
                        class="task-radio"
                    >

                    <span class="task-title">
                        ${title}
                    </span>

                </div>

                <div class="task-actions">

                    <button class="edit-button">
                        ✎
                    </button>

                    <button class="delete-button">
                        🗑
                    </button>

                </div>
            `;

  tasksContainer.appendChild(task);

  taskInput.value = "";

  addTaskEvents(task);
}

const taskForm = document.getElementById("taskForm");

taskForm.addEventListener("submit", function (event) {
  event.preventDefault();

  addTask();
});

// Task events
function addTaskEvents(task) {
  const radio = task.querySelector(".task-radio");
  const deleteButton = task.querySelector(".delete-button");
  const editButton = task.querySelector(".edit-button");

  // مقدار اولیه Radio
  radio.dataset.checked = radio.checked ? "true" : "false";

  // Complete / Uncomplete task
  radio.addEventListener("click", function (event) {
    if (radio.dataset.checked === "true") {
      radio.checked = false;
      radio.dataset.checked = "false";

      task.classList.remove("completed");
    } else {
      radio.checked = true;
      radio.dataset.checked = "true";

      task.classList.add("completed");
    }
  });

  // Delete task
  deleteButton.addEventListener("click", function () {
    task.remove();
  });

  // Edit task
  editButton.addEventListener("click", function () {
    const title = task.querySelector(".task-title");

    const newTitle = prompt(
      "عنوان جدید را وارد کنید:",
      title.textContent.trim(),
    );

    if (newTitle !== null && newTitle.trim() !== "") {
      title.textContent = newTitle.trim();
    }
  });
}

// Activate events for existing tasks
document.querySelectorAll(".task").forEach(addTaskEvents);
