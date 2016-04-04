#include <string>

using namespace std;

#ifndef TUTORIAL_H
#define TUTORIAL_H


class Tutorial {
    public:
        Tutorial();
        Tutorial(string title, string presenter, string link, int duration, int likes = 0);
        ~Tutorial();
        string getTitle();
        string getPresenter();
        string getLink();
        int getDuration();
        int getLikes();
        void setTitle(string title);
        void setPresenter(string presenter);
        void setLink(string link);
        void setDuration(int duration);
        void setLikes(int likes);
        string repr();
        static Tutorial fromString(string aux);
    private:
        string _title, _presenter, _link;
        int _duration;
        int _likes;
};

inline bool operator == (const Tutorial &x, const Tutorial &y) {
    return x.getLink() == y.getLink();
}

#endif // TUTORIAL_H
