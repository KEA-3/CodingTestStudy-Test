import java.util.*;

class Solution {
    public ArrayList<String> solution(String[] record) {
        
        HashMap<String, String> map = new HashMap<>();
        ArrayList<String> answer = new ArrayList<>(); // id : 닉네임
        
        for (String r : record){
            StringTokenizer str = new StringTokenizer(r, " ");
            
            String func = str.nextToken();
            String user = str.nextToken();
            
            if (func.equals("Enter")){
                // log에 id로 기록
                answer.add(user+"님이 들어왔습니다.");
                
                // id에 대한 닉네임 저장
                String nickname = str.nextToken();
                map.put(user, nickname);
                
            } else if ( func.equals("Leave") ){
                // log에 id로 기록
                answer.add(user+"님이 나갔습니다.");
                
            } else if ( func.equals("Change") ){
                // id에 대한 수정된 닉네임 저장
                String nickname = str.nextToken();
                map.put(user, nickname);
            }
            
        }
        
        // id를 닉네임으로 바꿔주기
        for (int i=0; i < answer.size(); i++){
            String[] log = answer.get(i).split("님이 ");
            String id = log[0];
            String action = log[1];
            answer.set(i, map.get(id) + "님이 "+ action);
        }
        
        return answer;
    }
    
    
}
