def lru_latex(frames, sequence):

    n = len(sequence)

    memory = []
    last_used = {}

    table = [[""]*n for _ in range(frames)]

    for i, page in enumerate(sequence):

        # ACIERTO
        if page in memory:
            row = memory.index(page)
            table[row][i] = f"\\acierto{{{page}}}"
            last_used[page] = i

        # FALLO
        else:

            if len(memory) < frames:
                memory.append(page)
                row = len(memory) - 1

            else:
                # encontrar la página menos recientemente usada
                lru_page = min(memory, key=lambda p: last_used[p])
                row = memory.index(lru_page)
                memory[row] = page
                del last_used[lru_page]

            table[row][i] = f"\\fallo{{{page}}}"
            last_used[page] = i

    # LATEX

    frame_labels = ",".join(str(i) for i in range(frames))
    seq_labels = ",".join(str(x) for x in sequence)

    out = []
    out.append(f"\\fifo{{{frame_labels}}}{{{seq_labels}}}")
    out.append("")

    for r in range(frames):
        fila = "    \\fila{" + "&".join(table[r]) + "}"
        out.append(fila)

    out.append("")
    out.append("\\endfifo")

    return "\n".join(out)


frames = int(input("Número de marcos: "))
sequence = list(map(int, input("Secuencia: ").split()))

print("\nCódigo LaTeX generado:\n")
print(lru_latex(frames, sequence))