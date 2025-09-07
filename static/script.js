function renderResults(result) {
  let html = "";
  if (typeof result === "object") {
    for (let key in result) {
      if (Array.isArray(result[key])) {
        html += `<div class="result-item"><span class="result-key">${key}:</span><ul>`;
        result[key].forEach(val => {
          html += `<li class="result-value">${JSON.stringify(val)}</li>`;
        });
        html += `</ul></div>`;
      } else if (typeof result[key] === "object") {
        html += `<div class="result-item"><span class="result-key">${key}:</span><pre class="result-value">${JSON.stringify(result[key], null, 2)}</pre></div>`;
      } else {
        html += `<div class="result-item"><span class="result-key">${key}:</span> <span class="result-value">${result[key]}</span></div>`;
      }
    }
  } else {
    html = `<div class="result-item">${result}</div>`;
  }
  return html;
}

async function startScan(type) {
  let target = prompt("Enter target URL (e.g. https://example.com):");
  let data = { target };

  if (type === "credentials") {
    data.username = prompt("Enter username:");
    data.password = prompt("Enter password:");
  }

  if (!target) return;

  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = `<div class="alert alert-info">⏳ Scanning ${target} with ${type}...</div>`;

  try {
    const res = await fetch(`/scan/${type}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
    const result = await res.json();
    resultsDiv.innerHTML = renderResults(result);
  } catch (err) {
    resultsDiv.innerHTML = `<div class="alert alert-danger">Error: ${err.message}</div>`;
  }
}
