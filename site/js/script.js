/* AI Photo Organizing Guide — Table of Contents builder */
document.addEventListener("DOMContentLoaded", () => {
  const tocList = document.getElementById("toc-list");
  const headings = document.querySelectorAll("#content h2");

  headings.forEach((heading) => {
    const id = heading.id;
    const text = heading.textContent;

    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = "#" + id;
    a.textContent = text;
    li.appendChild(a);
    tocList.appendChild(li);
  });
});