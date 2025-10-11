def pythonScript = "weather_etl.py"

// Run the Python script
def process = ["python3", pythonScript].execute()
process.in.eachLine { line ->
    println line
}
process.err.eachLine { line ->
    System.err.println "ERROR: $line"
}

int exitCode = process.waitFor()
if (exitCode == 0) {
    println "Python script executed successfully."
} else {
    println "Python script failed with exit code: $exitCode"
}
