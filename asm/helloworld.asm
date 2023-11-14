; print .386 //print hello_world
; Dies ist ein Kommentar, der die Bedeutung des Codes beschreibt.
DATA SEGMENT USE16
; Beginn des Datensegments, das im 16-Bit-Modus verwendet wird.
MESG DB 'Hello python','$'
; Definiert eine Zeichenfolge mit dem Text 'Hello python' gefolgt von einem Nullbyte ($).
; Die Zeichenfolge wird MESG genannt und im Datensegment platziert.
DATA ENDS
; Ende des Datensegments.
CODE SEGMENT USE16
; Beginn des Codesegments, das im 16-Bit-Modus verwendet wird.
    ASSUME CS:CODE,DS:DATA
    ; Die Segmentregistrieren werden festgelegt, um auf das Code- und Datensegment zuzugreifen.
BEG: ; Ein Label mit dem Namen "BEG" markiert den Beginn des Programms.
    MOV AX,DATA ; Die Adresse des Datensegments wird in AX geladen.
    MOV DS,AX ; Der Datenzeiger (DS) wird auf die Adresse im Register AX gesetzt, um auf das Datensegment zuzugreifen.
    MOV AH,9 ; Der Wert 9 wird in das AH-Register geladen, um den DOS-Dienst 9 (Drucken von Zeichenfolgen) aufzurufen.
    MOV DX, OFFSET MESG ; Die Adresse der Zeichenfolge MESG wird in das DX-Register geladen.
    INT 21H ; Ein Software-Interrupt 21H wird ausgelöst, um den DOS-Dienst 9 (Drucken von Zeichenfolgen) aufzurufen.
    MOV AH,4CH ; Der Wert 4CH wird in das AH-Register geladen, um den DOS-Dienst 4CH (Programm beenden) aufzurufen.
    INT 21H ; Ein Software-Interrupt 21H wird ausgelöst, um das Programm zu beenden und zur DOS-Umgebung zurückzukehren.
CODE ENDS
; Ende des Codesegments.
END BEG
; Das Programmende wird markiert und auf das Label "BEG" verwiesen.