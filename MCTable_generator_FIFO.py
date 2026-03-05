from collections import deque

def fifo_latex(frames, sequence):

    n = len(sequence)

    memory = []
    queue = deque()

    frame_table = [[""]*n for _ in range(frames)]

    for i, page in enumerate(sequence):

        if page in memory:
            row = memory.index(page)
            frame_table[row][i] = f"\\acierto{{{page}}}"

        else:

            if len(memory) < frames:
                memory.append(page)
                queue.append(page)
                row = len(memory)-1

            else:
                old = queue.popleft()
                row = memory.index(old)
                memory[row] = page
                queue.append(page)

            frame_table[row][i] = f"\\fallo{{{page}}}"

    # LATEX

    frame_labels = ",".join(str(i) for i in range(frames))
    seq_labels = ",".join(str(x) for x in sequence)

    latex = []
    latex.append(f"\\fifo{{{frame_labels}}}{{{seq_labels}}}")
    latex.append("")

    for f in range(frames):
        fila = "    \\fila{" + "&".join(frame_table[f]) + "}"
        latex.append(fila)

    latex.append("")
    latex.append("\\endfifo")

    return "\n".join(latex)

frames = int(input("Número de marcos: "))
sequence = list(map(int, input("Secuencia (separada por espacios): ").split()))

print("\nCódigo LaTeX generado:\n")
print(fifo_latex(frames, sequence))