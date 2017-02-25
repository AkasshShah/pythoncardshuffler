import java.util.*;
public class CardShuffler{
   public static String[] genUnshuffledCards(){
      String[] cardNumbers={"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"};
      String[] cardSuites={"Spades","Clubs","Hearts","Diamonds"};
      String[] unshuffledDeck= new String[52];
      int k=0;
      for(int i=0;i<cardSuites.length;i++){
         for(int j=0;j<cardNumbers.length;j++){
            unshuffledDeck[k]=cardNumbers[j]+" of "+cardSuites[i];
            //System.out.println(k);
            k++;
         }
      }
      return(unshuffledDeck);
   }
   public static String[] shuffleDeck(String[] deckOfCards){
      String[] shuffledDeck={"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""};
      int m=0;
      for(int a=0;a<deckOfCards.length;a++){
         for(int n=0;n<52;n++){
            m=(int) Math.random()*52;
            if(shuffledDeck[m]==""){
               shuffledDeck[m]=deckOfCards[a];
               break;
            }
            else{
               m=(int) Math.random()*52;
            }
         }
      }
      return(shuffledDeck);
   }
   public static void main(String[] args){
      String[] originalDeck=genUnshuffledCards();
      System.out.println("Unshuffled Deck is:");
      for(int i=0;i<originalDeck.length;i++){
         System.out.println(originalDeck[i]);
      }
      String[] shuffleddDeck=shuffleDeck(originalDeck);
      //System.out.println(shuffleddDeck.length);
      System.out.println("Shuffled Deck is: ");
      for(int j=0;j<shuffleddDeck.length;j++){
         System.out.println(shuffleddDeck[j]);
      }
   }
}