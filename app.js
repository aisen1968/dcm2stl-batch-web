async function convert() {
  const files = document.getElementById("files").files;
  const formData = new FormData();

  for (let file of files) {
    formData.append("files", file);
  }

  const response = await fetch("/convert", {
    method: "POST",
    body: formData
  });

  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "DCM_to_STL_result.zip";
  a.click();
}
