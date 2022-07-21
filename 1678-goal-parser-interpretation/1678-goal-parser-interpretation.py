class Solution:
    def interpret(self, command: str) -> str:
        i=0
        op=""
        while i!=len(command):
            if command[i]=="G":
                op+="G"
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                op+="o"
                i+=2
            elif command[i]=="(" and command[i+1]=="a":
                op+="al"
                i+=4
        return op
        