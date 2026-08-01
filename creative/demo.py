from .core import Concept,approve
def main():
 c=Concept("Local service story","show a before/after workflow",["gold and navy brand","no generated text in image"],"A service operator reviewing a clear workflow diagram.","generated concept; final asset review required")
 print(approve(c))
if __name__=="__main__": main()
