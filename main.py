from js import document

def compute_average(*args, **kwargs):
    try:
        g1 = float(document.getElementById("grade1").value)
        g2 = float(document.getElementById("grade2").value)
        g3 = float(document.getElementById("grade3").value)
        g4 = float(document.getElementById("grade4").value)
        avg = (g1 + g2 + g3 + g4) / 4

        document.getElementById("average").innerText = f"{avg:.2f}"

        result_element = document.getElementById("result")
        place_element = document.getElementById("place")

        if avg >= 95:
            place_element.innerText = "Top of the Class 🏆"
            result_element.className = "passed"
            result_element.innerText = "Yes ✅"

        elif avg >= 85:
            place_element.innerText = "Passed✅"
            result_element.className = "passed"
            result_element.innerText = "Yes ✅"

        else:
            place_element.innerText = "Failed❌"
            result_element.className = "failed"
            result_element.innerText = "No ❌"

    except Exception:
        document.getElementById("average").innerText = "N/A"
        place_element = document.getElementById("place")
        result_element = document.getElementById("result")
        result_element.className = "failed"
        result_element.innerText = "Invalid input ⚠️"