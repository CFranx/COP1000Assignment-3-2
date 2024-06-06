#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank


def testScoreRank():
  testScore = int(input("Student's test score: "))
  classRank = int(input("Student's class rank: "))
  # Test using admission requirements and print Accept or Reject
  if testScore >= 90:
    if classRank >= 25:
      print("Accept")
      return "Accept"
    else:
      print("Reject")
      return "Reject"
  else:
    if testScore >= 80:
      if classRank >= 50:
        print("Accept")
        return "Accept"
      else:
        print("Reject")
        return "Reject"
    else:
      if testScore >= 70:
        if classRank >= 75:
          print("Accept")
          return "Accept"
        else:
          print("Reject")
          return "Reject"
      else:
        print("Reject")
        return "Reject"


if __name__ == "__main__":
  testScoreRank()
