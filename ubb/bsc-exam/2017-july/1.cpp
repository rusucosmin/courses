#include <iostream>
#include <vector>

using namespace std;;

class Fruit {
private:
  bool withSeeds;
public:
  Fruit(bool withSeeds) {
    this->withSeeds = withSeeds;
  }
  virtual string getDescription() = 0;
  bool isWithSeeds() {
    return this->withSeeds;
  }
};

class MelonLike: public Fruit {
private:
  double kg;
public:
  MelonLike(double kg, bool withSeeds): Fruit(withSeeds) {
    assert(kg > 0);
    this->kg = kg;
  }
  virtual string getDescription() {
    return to_string(kg) + (
      this->isWithSeeds() ? "with seeds" : "without seeds"
    );
  }
};

class Melon: public MelonLike {
public:
  Melon(double kg, bool withSeeds): MelonLike(kg, withSeeds) {
  }
  virtual string getDescription() {
    return MelonLike::getDescription() + "melon";
  }
};

class Watermelon : public MelonLike {
public:
  Watermelon(double kg, bool withSeeds): MelonLike(kg, withSeeds) {
  }
  virtual string getDescription() {
    return MelonLike::getDescription() + "watermelon";
  }
};

int getInsertPosition(vector <Fruit*> v, Fruit* f) {
  int st = 0, dr = v.size() - 1;
  int ret = v.size();
  while(st <= dr) {
    cerr << st << ' ' << dr << '\n';
    int mid = (st + dr) / 2;
    if(f->getDescription() <= v[mid]->getDescription()) {
      ret = mid;
      dr = mid - 1;
    } else {
      st = mid + 1;
    }
  }
  return ret;
}

vector <Fruit*> insertFruit(vector <Fruit*> v, Fruit* f) {
  int pos = getInsertPosition(v, f);
  v.insert(v.begin() + pos, f);
  return v;
}
vector <Fruit*> filter(vector <Fruit*> v, bool withSeeds) {
  vector <Fruit*> ret;
  for(auto it : v) {
    if(it->isWithSeeds() == withSeeds) {
      ret.push_back(it);
    }
  }
  return ret;
}

int main() {
  vector <Fruit*> v;
  v.push_back(new Melon(10, true));
  v.push_back(new MelonLike(11, false));
  v.push_back(new Watermelon(13, true));
  v.push_back(new Watermelon(6, false));
  v = insertFruit(v, new Watermelon(12, true));
  cerr << "insert\n";
  for(auto it : v) {
    cerr << it->getDescription() << '\n';
  }
  cerr << "withoutSeeds\n";
  for(auto it : filter(v, false)) {
    cerr << it->getDescription() << '\n';
  }
  cerr << "withSeeds\n";
  for(auto it : filter(v, true)) {
    cerr << it->getDescription() << '\n';
  }
}

